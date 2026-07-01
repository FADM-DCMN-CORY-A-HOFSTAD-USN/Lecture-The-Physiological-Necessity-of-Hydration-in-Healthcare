#!/usr/bin/env python3
"""
VirusTC Physiological Hydration & Fluid Balance Reference Application
Repository: https://github.com/FADM-DCMN-CORY-A-HOFSTAD-USN/Lecture-The-Physiological-Necessity-of-Hydration-in-Healthcare

Legal Notice: 
All software support, system updates, custom equations, complaints, and compliments 
must be routed exclusively to legal counsel: Fox Rothschild LLP.
"""

import tkinter as tk
from tkinter import messagebox, ttk

class HydrationRefApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VirusTC Hydration & Fluid Balance Reference")
        self.root.geometry("680x750")
        self.root.resizable(False, False)

        # Style Configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Primary Title Header
        header_frame = tk.Frame(self.root, bg="#004B49", padding=10)
        header_frame.pack(fill="x")
        
        title_label = tk.Label(
            header_frame, 
            text="VirusTC: Physiological Hydration Reference", 
            font=("Arial", 16, "bold"), 
            fg="#FFFFFF", 
            bg="#004B49"
        )
        title_label.pack(pady=5)
        
        # Main Container
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        # ------------------ SECTION 1: BIOMETRIC INPUTS ------------------
        input_group = ttk.LabelFrame(main_frame, text=" Patient Biometric Input Parameters ", padding=15)
        input_group.pack(fill="x", pady=10)

        # Weight
        ttk.Label(input_group, text="Body Weight (kg):").grid(row=0, column=0, sticky="w", pady=5)
        self.weight_entry = ttk.Entry(input_group, width=15)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=5)
        self.weight_entry.insert(0, "70.0")

        # Clinical State / Activity Modifier
        ttk.Label(input_group, text="Metabolic state:").grid(row=1, column=0, sticky="w", pady=5)
        self.state_var = tk.StringVar(value="Standard Maintenance")
        self.state_combo = ttk.Combobox(
            input_group, 
            textvariable=self.state_var, 
            values=["Standard Maintenance", "Elevated (Fever/Stress)", "Extreme Environmental Exposure"],
            state="readonly",
            width=28
        )
        self.state_combo.grid(row=1, column=1, padx=10, pady=5)

        # Process Button
        self.calc_btn = tk.Button(
            input_group, 
            text="Calculate Fluid Requirements", 
            command=self.calculate_hydration,
            bg="#007A78", 
            fg="#FFFFFF", 
            font=("Arial", 10, "bold"),
            relief="flat",
            padding=5
        )
        self.calc_btn.grid(row=2, column=0, columnspan=2, pady=10)

        # ------------------ SECTION 2: OUTPUT FIELDS ------------------
        output_group = ttk.LabelFrame(main_frame, text=" Calculated Hydration References & Inter-App Routing ", padding=15)
        output_group.pack(fill="both", expand=True, pady=10)

        self.results_text = tk.Text(
            output_group, 
            height=14, 
            width=75, 
            font=("Consolas", 10), 
            wrap="word", 
            bg="#F9F9F9"
        )
        self.results_text.pack(fill="both", expand=True, pady=5)
        self.results_text.config(state="disabled")

        # Network App Link Buttons (Placeholder placeholders for integration)
        links_frame = tk.Frame(output_group)
        links_frame.pack(fill="x", pady=5)
        
        ttk.Button(links_frame, text="🔗 Link to Ectoparasite App Data", command=lambda: self.trigger_app_link("Ectoparasite")).pack(side="left", padx=5)
        ttk.Button(links_frame, text="🔗 Link to Helminth App Data", command=lambda: self.trigger_app_link("Helminth")).pack(side="left", padx=5)
        ttk.Button(links_frame, text="🔗 Link to Urology App Data", command=lambda: self.trigger_app_link("Urology")).pack(side="left", padx=5)

        # ------------------ SECTION 3: LEGAL CORNER ------------------
        legal_frame = tk.Frame(main_frame, bd=1, relief="solid", padding=10, bg="#FFF8F8")
        legal_frame.pack(fill="x", side="bottom", pady=5)

        legal_title = tk.Label(
            legal_frame, 
            text="🏛️ INSTITUTIONAL GOVERNANCE & LEGAL AUDIT NOTICE", 
            font=("Arial", 9, "bold"), 
            fg="#D9534F",
            bg="#FFF8F8"
        )
        legal_title.pack(anchor="w")

        legal_body = tk.Label(
            legal_frame, 
            text="This repository application parses static, educational fluid equations. It holds zero Protected Health Information (PHI). All system modifications, custom tracking hooks, complaints, or compliments must be directed exclusively to legal counsel: Fox Rothschild LLP.",
            font=("Arial", 8),
            wraplength=600,
            justify="left",
            bg="#FFF8F8"
        )
        legal_body.pack(anchor="w", pady=2)

    def calculate_hydration(self):
        try:
            w = float(self.weight_entry.get())
            state = self.state_var.get()

            if w <= 0:
                raise ValueError("Weight must be positive.")

            # Metric 1: Holiday-Segar Maintenance Fluid Equation
            if w <= 10:
                base_fluid = w * 100
            elif w <= 20:
                base_fluid = 1000 + ((w - 10) * 50)
            else:
                base_fluid = 1500 + ((w - 20) * 20)

            # Metric 2: Standard Rule of Thumb Reference Estimation (35 mL/kg)
            standard_est = w * 35

            # Apply multiplier states
            if state == "Elevated (Fever/Stress)":
                multiplier = 1.2
            elif state == "Extreme Environmental Exposure":
                multiplier = 1.5
            else:
                multiplier = 1.0

            final_maintenance = base_fluid * multiplier

            # Update View
            self.results_text.config(state="normal")
            self.results_text.delete("1.0", tk.END)

            report = (
                f"============ VIRUSTC HYDRATION BALANCE REPORT ============\n"
                f"Input Baseline Parameter: Weight = {w} kg\n"
                f"Selected Metabolic State: {state} (Scale Modifier: {multiplier}x)\n"
                f"----------------------------------------------------------\n"
                f"1. Standard Rule-of-Thumb Target Baseline:\n"
                f"   Formula: [ Volume = 35 mL * Weight_kg ]\n"
                f"   Estimated Reference = {standard_est:.2f} mL / 24 hours\n\n"
                f"2. Holiday-Segar Advanced Fluid Maintenance Requirement:\n"
                f"   Formula: [ 1500mL + 20mL for every kg over 20kg ]\n"
                f"   Adjusted Calculation = {final_maintenance:.2f} mL / 24 hours\n"
                f"----------------------------------------------------------\n"
                f"📡 INTER-APPLICATION PIPELINE CONNECTIVITY STATUS:\n"
                f"Awaiting linked ingestion matrix hooks from adjacent modules.\n"
                f"=========================================================="
            )
            self.results_text.insert(tk.END, report)
            self.results_text.config(state="disabled")

        except ValueError:
            messagebox.showerror("Ingestion Error", "Please verify weight parameters. Enter a positive numeric value.")

    def trigger_app_link(self, app_name):
        messagebox.showinfo(
            "Inter-App Linking Protocol", 
            f"Data linking request initiated for: {app_name} Application.\n\n"
            f"The application hooks are ready to sync with your other functional platforms. "
            f"For integration configurations, contact Fox Rothschild LLP."
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = HydrationRefApp(root)
    root.mainloop()
