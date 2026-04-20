import json, time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress

console = Console()

class SafetyAgent:
    def __init__(self):
        self.node = "N-1 Nairobi"
        self.role = "Assistant Storekeeper (Carnival Context)"
        self.drill_status = "STNDBY"

    def execute_drill_simulation(self):
        console.print(Panel.fit(
            "[bold red]🚢 EMERGENCY DRILL INITIATED: ABANDON SHIP[/bold red]\n"
            "Muster Station: [bold yellow]STATION D - DECK 4[/bold yellow]",
            border_style="red"
        ))

        tasks = [
            ("Isolating Storehouse Equipment", 2),
            ("Securing Hazardous Chemicals", 1.5),
            ("Activating Public Area Clearance", 2),
            ("Reporting to Muster Station D", 1)
        ]

        with Progress() as progress:
            task_id = progress.add_task("[cyan]Executing Emergency Protocols...", total=len(tasks))
            for task_name, duration in tasks:
                console.print(f"[dim]Action:[/dim] {task_name}...")
                time.sleep(duration)
                progress.update(task_id, advance=1)

    def log_compliance(self):
        log = {
            "timestamp": datetime.now().isoformat(),
            "drill_type": "Abandon Ship / General Emergency",
            "compliance_standard": "SOLAS 2026 / HESS",
            "personnel_status": "VERIFIED - FULL PARTICIPATION",
            "storehouse_integrity": "SECURED"
        }
        with open('safety_drill_log.json', 'w') as f:
            json.dump(log, f, indent=4)
        console.print("\n[bold green]✔ Safety Drill Manifest logged to safety_drill_log.json[/bold green]")

if __name__ == "__main__":
    agent = SafetyAgent()
    agent.execute_drill_simulation()
    agent.log_compliance()
