from datetime import datetime


def generate_report(input_file="system_logs.txt", output_file="daily_report.txt"):
    info_count = 0
    warning_count = 0
    error_count = 0
    critical_lines = []

    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue

            if "[INFO]" in clean_line:
                info_count += 1
            elif "[WARNING]" in clean_line:
                warning_count += 1
                critical_lines.append(clean_line)
            elif "[ERROR]" in clean_line:
                error_count += 1
                critical_lines.append(clean_line)

    if error_count > 0:
        health_status = "CRITICAL (Errors detected)"
    elif warning_count > 0:
        health_status = "WARNING (Attention recommended)"
    else:
        health_status = "HEALTHY"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_content = [
        "=== SYSTEM HEALTH & LOG REPORT ===",
        f"Generated at: {timestamp}",
        f"Overall Status: {health_status}",
        "",
        "Summary:",
        f"- INFO events:    {info_count}",
        f"- WARNING events: {warning_count}",
        f"- ERROR events:   {error_count}",
        "",
        "Warnings & Errors Details:",
    ]

    if critical_lines:
        report_content.extend(f"  * {item}" for item in critical_lines)
    else:
        report_content.append("  * No warnings or errors found.")

    with open(output_file, "w", encoding="utf-8") as report:
        report.write("\n".join(report_content) + "\n")

    print(f"Report generated successfully in '{output_file}'.")


if __name__ == "__main__":
    generate_report()