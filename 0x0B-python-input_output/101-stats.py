import sys
from collections import defaultdict
"""A class for computing and printing log metrics"""


class LogMetrics:
    """
    Attributes:
        total_size (int): Total file size sum.
        status_code_counts (dict): Counts of each status code.
        line_number (int): Number of lines processed.
    """
    def __init__(self):
        """Initialize LogMetrics instance."""
        self.total_size = 0
        self.status_code_counts = defaultdict(int)
        self.line_number = 0

    def process_line(self, line):
        """Process a log line and update metrics."""
        self.line_number += 1

        parts = line.split()
        if len(parts) < 10:
            return

        status_code = parts[-2]
        file_size = int(parts[-1])

        self.total_size += file_size

        if status_code in {
                "200", "301", "400", "401",
                "403", "404", "405", "500"
                }:
            self.status_code_counts[status_code] += 1

        if self.line_number % 10 == 0:
            self.print_statistics()

    def print_statistics(self):
        """Print computed log metrics."""

        print("Total file size: File size:", self.total_size)
        for code in sorted(self.status_code_counts.keys()):
            print(f"{code}: {self.status_code_counts[code]}")


if __name__ == "__main__":
    metrics = LogMetrics()

    try:
        for line in sys.stdin:
            metrics.process_line(line)
    except KeyboardInterrupt:
        metrics.print_statistics()
