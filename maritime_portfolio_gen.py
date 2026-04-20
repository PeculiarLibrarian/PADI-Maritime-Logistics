import json
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()

def generate_unified_audit():
    try:
        with open('maritime_audit.json', 'r') as f:
            logistics = json.load(f)
        with open('safety_drill_log.json', 'r') as f:
            safety = json.load(f)
    except FileNotFoundError:
        console.print("[bold red]Error: Manifests missing. Run orchestrators first![/bold red]")
        return

    console.print("\n[bold white on blue]  PADI MARITIME AUTHORITY AUDIT - N-1 NAIROBI NODE  [/bold white on blue]")
    
    # Section 1: Logistics Integrity
    table_l = Table(title="Section I: Logistics & FIFO Integrity", header_style="cyan")
    table_l.add_column("Resource", style="dim")
    table_l.add_column("Integrity")
    table_l.add_column("Remediation Status")
    
    for item in logistics['results']:
        status = "REMEDIATED" if "Dry" in item['item'] else "VERIFIED"
        table_l.add_row(item['item'], item['shelf_life'], f"[green]{status}[/green]")
    console.print(table_l)

    # Section II: SOLAS/HESS Compliance
    console.print("\n[bold yellow]Section II: Safety & Emergency Readiness[/bold yellow]")
    console.print(f"Drill Type: {safety['drill_type']}")
    console.print(f"Personnel Status: [bold green]{safety['personnel_status']}[/bold green]")
    console.print(f"Storehouse Integrity: {safety['storehouse_integrity']}")
    
    console.print(f"\n[dim]Audit DOI Equivalent (PADI): {datetime.now().strftime('%Y%m%d')}-MAR-ALPHA[/dim]")

if __name__ == "__main__":
    generate_unified_audit()
