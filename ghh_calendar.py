"""
Greek-Hanke-Henry Permanent Calendar (GHH)

This program implements the Greek-Hanke-Henry Permanent Calendar (GHH), a
fixed calendar system designed to resolve the inefficiencies of the Gregorian
calendar while maintaining compatibility with the 7-day week and modern
software standards.

Key Features:
-------------
1.  **Structure**: The year is divided into 4 identical quarters.
    - Pattern: 30 days, 30 days, 31 days.
    - Total: (30+30+31) * 4 = 364 days (52 Weeks).
    
2.  **Naming Convention**:
    - Uses Greek Alphabet (Alpha - Mu) for months to ensure global neutrality.
      
3.  **Synchronization (ISO-8601)**:
    - "Alpha 1" is anchored to the Monday of ISO Week 1.

4.  **Leap Logic (Omega Week)**:
    - Instead of a leap day, a "Leap Week" named OMEGA is added every 5-6 years
      (whenever the ISO year has 53 weeks).
      
Author: Gemini 3 Pro
Vibe-Coder: Dennis WK Khong
"""

import datetime
import sys

# --- CONSTANTS ---
WARNING_PROLEPTIC = (
    "   [!] WARNING: Dates prior to Oct 15, 1582 are rendered in the \n"
    "       Proleptic Gregorian system and may not correspond to historical \n"
    "       Julian dates."
)
CUTOFF_DATE = datetime.date(1582, 10, 15)

class GreekHankeHenryCalendar:
    def __init__(self):
        # 30-30-31 Pattern (Quarterly)
        self.month_structure = [30, 30, 31, 30, 30, 31, 30, 30, 31, 30, 30, 31]
        
        # Omega is at index 12
        self.month_names = [
            "Alpha", "Beta", "Gamma", 
            "Delta", "Epsilon", "Zeta", 
            "Eta", "Theta", "Iota", 
            "Kappa", "Lambda", "Mu",
            "Omega" 
        ]
        
        # Fixed starting weekdays (0=Mon, 2=Wed, 4=Fri)
        self.fixed_start_days = [0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4]
        self.week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        # --- BOX DRAWING CONSTANTS ---
        self.H_LINE = "─"
        self.V_LINE = "│"
        self.TOP_LEFT  = "┌"
        self.TOP_MID   = "┬"
        self.TOP_RIGHT = "┐"
        self.MID_LEFT  = "├"
        self.MID_CROSS = "┼"
        self.MID_RIGHT = "┤"
        self.BOT_LEFT  = "└"
        self.BOT_MID   = "┴"
        self.BOT_RIGHT = "┘"
        self.CELL_WIDTH = 14  

    def _print_divider(self, left, mid, right):
        """Helper to print a horizontal divider line"""
        segment = self.H_LINE * self.CELL_WIDTH
        line = left + (segment + mid) * 6 + segment + right
        print(line)

    def print_month_grid(self, month_name, days_in_month, start_greg_date, start_weekday_idx):
        """Prints a solid grid for the month."""
        print(f"\n {month_name.upper()} ({days_in_month} Days)")
        
        self._print_divider(self.TOP_LEFT, self.TOP_MID, self.TOP_RIGHT)
        
        header_row = self.V_LINE
        for d in self.week_days:
            header_row += f"{d:^{self.CELL_WIDTH}}{self.V_LINE}"
        print(header_row)
        
        self._print_divider(self.MID_LEFT, self.MID_CROSS, self.MID_RIGHT)

        current_greg_date = start_greg_date
        current_day = 1
        day_of_week = 0
        
        row_buffer = self.V_LINE
        
        # Padding for empty start slots
        empty_slots = start_weekday_idx
        for _ in range(empty_slots):
            row_buffer += " " * self.CELL_WIDTH + self.V_LINE
            day_of_week += 1

        while current_day <= days_in_month:
            g_str = current_greg_date.strftime("%b %d")
            cell_text = f"{current_day:02d} ({g_str})"
            
            row_buffer += f"{cell_text:^{self.CELL_WIDTH}}{self.V_LINE}"
            
            current_day += 1
            current_greg_date += datetime.timedelta(days=1)
            day_of_week += 1

            if day_of_week == 7:
                print(row_buffer)
                if current_day <= days_in_month:
                    self._print_divider(self.MID_LEFT, self.MID_CROSS, self.MID_RIGHT)
                row_buffer = self.V_LINE
                day_of_week = 0

        if day_of_week != 0:
            remaining = 7 - day_of_week
            for _ in range(remaining):
                row_buffer += " " * self.CELL_WIDTH + self.V_LINE
            print(row_buffer)

        self._print_divider(self.BOT_LEFT, self.BOT_MID, self.BOT_RIGHT)

    def generate_year_calendar(self, year):
        # --- CHECK WARNING ---
        # If year is 1582 or earlier, warn about Proleptic Gregorian usage.
        if year < 1583:
            print(f"\n{WARNING_PROLEPTIC}")

        print(f"\n{'#'*90}")
        print(f"   GREEK-HANKE-HENRY PERMANENT CALENDAR (GHH) :: YEAR {year}")
        print(f"{'#'*90}")

        try:
            jan4 = datetime.date(year, 1, 4)
        except ValueError:
            print("Error: Year out of range for standard calendar functions.")
            return

        start_of_year = jan4 - datetime.timedelta(days=jan4.isoweekday() - 1)
        current_greg_date = start_of_year
        
        # Only iterate through the first 12 months (indices 0-11)
        for i in range(12):
            name = self.month_names[i]
            length = self.month_structure[i]
            start_weekday = self.fixed_start_days[i]
            self.print_month_grid(name, length, current_greg_date, start_weekday)
            current_greg_date += datetime.timedelta(days=length)

        # Check Omega Week (Index 12)
        if current_greg_date.isocalendar()[0] == year:
            self.print_month_grid(self.month_names[12], 7, current_greg_date, 0)
        else:
            print("\n [INFO] No Omega Week this year.")
            
    def gregorian_to_ghh(self, date_obj):
        """Converts Gregorian date to GHH Date"""
        iso_year, iso_week, iso_day = date_obj.isocalendar()
        
        if iso_week == 53:
            return {
                "year": iso_year,
                "month": self.month_names[12], # Omega
                "day": iso_day,
                "weekday": self.week_days[iso_day - 1],
                "is_omega": True
            }

        day_of_year_idx = (iso_week - 1) * 7 + (iso_day - 1)
        days_sum = 0
        
        for i in range(12):
            length = self.month_structure[i]
            if day_of_year_idx < days_sum + length:
                day_in_month = day_of_year_idx - days_sum + 1
                return {
                    "year": iso_year,
                    "month": self.month_names[i],
                    "day": day_in_month,
                    "weekday": self.week_days[iso_day - 1],
                    "is_omega": False
                }
            days_sum += length
        return None

    def ghh_to_gregorian(self, year, month_num, day):
        """Converts GHH Date (Year, Month Num 1-13, Day) to Gregorian"""
        
        # Using Jan 4 to find start of ISO year
        jan4 = datetime.date(year, 1, 4)
        alpha_1 = jan4 - datetime.timedelta(days=jan4.isoweekday() - 1)

        if not (1 <= month_num <= 13):
            return None, "Invalid month number. Must be 1-12 (or 13 for Omega)."
        
        max_days = 0
        is_omega = False
        
        if month_num == 13:
            start_week_53 = alpha_1 + datetime.timedelta(days=364)
            if start_week_53.isocalendar()[0] != year:
                return None, f"GHH Year {year} is not a leap year (No Month 13/Omega)."
            max_days = 7
            is_omega = True
        else:
            max_days = self.month_structure[month_num - 1]
            
        if not (1 <= day <= max_days):
            return None, f"Invalid day for Month {month_num}. Max is {max_days}."

        days_offset = 0
        if is_omega:
            days_offset = 364
        else:
            for i in range(month_num - 1):
                days_offset += self.month_structure[i]
        
        days_offset += (day - 1)
        result_date = alpha_1 + datetime.timedelta(days=days_offset)
        return result_date, None

# --- MENU SYSTEM ---

def get_valid_date(prompt="Enter Gregorian Date (YYYY-MM-DD): "):
    while True:
        try:
            date_str = input(prompt)
            # Standard Python datetime supports proleptic dates (0001-9999)
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid format or out of range. Please use YYYY-MM-DD.")

def get_valid_year():
    while True:
        try:
            year_str = input("Enter Year (YYYY): ")
            return int(year_str)
        except ValueError:
            print("Invalid integer.")

def get_ghh_input_string():
    print("\n   Enter GHH Date (YYYY-MM-DD)")
    print("   * Use Month 1-12 for Alpha-Mu")
    print("   * Use Month 13 for Omega (Leap Week)")
    
    while True:
        try:
            date_str = input("   > Input: ")
            parts = date_str.split('-')
            if len(parts) != 3:
                raise ValueError
            
            y = int(parts[0])
            m = int(parts[1])
            d = int(parts[2])
            return y, m, d
        except ValueError:
            print("   Invalid format. Please use YYYY-MM-DD (e.g., 2026-01-15 or 2026-13-05).")

def main():
    cal = GreekHankeHenryCalendar()
    
    while True:
        print("\n--- GREEK-HANKE-HENRY PERMANENT CALENDAR ---")
        print("1. Convert Gregorian Date -> GHH Date")
        print("2. Convert GHH Date -> Gregorian Date")
        print("3. Generate GHH Annual Calendar")
        print("0. Exit")
        
        choice = input("Select option (0-3): ")
        
        if choice == '1':
            g_date = get_valid_date("Enter Gregorian Date (YYYY-MM-DD): ")
            
            # --- CHECK WARNING ---
            if g_date < CUTOFF_DATE:
                print(f"\n{WARNING_PROLEPTIC}")

            f_date = cal.gregorian_to_ghh(g_date)
            
            print(f"\n>> RESULT: {g_date.strftime('%Y-%m-%d')} is...")
            print(f"   {f_date['year']} {f_date['month'].upper()} {f_date['day']}")
            print(f"   ({f_date['weekday']})")
            
            if f_date['is_omega']:
                print("   * Note: This falls in the Leap Week (Omega) *")

        elif choice == '2':
            y, m, d = get_ghh_input_string()
            
            res_date, error = cal.ghh_to_gregorian(y, m, d)
            
            if error:
                print(f"\n>> ERROR: {error}")
            else:
                m_name = cal.month_names[m-1] 
                
                # --- DETERMINE LABEL & CHECK WARNING ---
                label = "Gregorian"
                if res_date < CUTOFF_DATE:
                    print(f"\n{WARNING_PROLEPTIC}")
                    label = "Proleptic Gregorian"

                print(f"\n>> RESULT: GHH {y} {m_name} {d} is...")
                print(f"   {label}: {res_date.strftime('%A, %Y-%m-%d')}")

        elif choice == '3':
            year = get_valid_year()
            cal.generate_year_calendar(year)
            
        elif choice == '0':
            print("Exiting. Goodbye!")
            sys.exit()
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()