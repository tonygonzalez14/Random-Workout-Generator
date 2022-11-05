# Random Workout Generator
import tkinter as tk
import random

class workout_GUI:
    def __init__(self): #constructor
        self.window = tk.Tk()
        self.window.title("Random Workout Generator") #window title
        self.window.geometry("325x350")
        self.workout_option_text = tk.Label(self.window, text="Enter desired workout number \nWorkout Options: \n1: Push \n2: Pull \n3: Legs \n4: Upper \n5: Lower").grid(row=0, column=0)
        self.workout_option = tk.StringVar()
        self.workout_option_entry = tk.Entry(self.window, width = 2, textvariable= self.workout_option).grid(row=0, column=1) #entry box
        self.generate_button = tk.Button(self.window, text="Generate", command=self.workout_generator).grid(row=1, column=0) #button   

        self.window.mainloop() 

    #workout generator function
    def workout_generator(self):
        option = int(self.workout_option.get())

        if option == 1: #push day
            self.generate_button = tk.Button(self.window, text="Regenerate", command=self.workout_generator).grid(row=1, column=0)
            self.workout_title = tk.Label(self.window, text="Your Push Workout:").grid(row=2, column=0) #title
            self.generated_mid_chest = tk.Label(self.window, text=self.mid_chest_exercise("mid_chest.txt")+ " 3x6-8").grid(row=3, column=0)
            self.generated_upper_chest = tk.Label(self.window, text=self.upper_chest_exercise("upper_chest.txt")+ " 3x10-12" ).grid(row=4, column=0)
            self.generated_lower_chest = tk.Label(self.window, text=self.lower_chest_exercise("lower_chest.txt")+ " 3x10-12").grid(row=5, column=0)
            self.generated_front_delt = tk.Label(self.window, text=self.front_delt_exercise("front_delt.txt")+ " 3x8-10").grid(row=6, column=0)
            self.generated_lateral_delt1 = tk.Label(self.window, text=self.lateral_delt_exercise("lateral_delt.txt")+ " 3x12-15").grid(row=7, column=0)
            self.generated_lateral_delt2 = tk.Label(self.window, text=self.lateral_delt_exercise("lateral_delt.txt")+ " 3x15-18").grid(row=8, column=0)
            self.generated_tricep = tk.Label(self.window, text=self.tricep_exercise("tricep.txt")+ " 3x10-12").grid(row=9, column=0)
            
        elif option == 2: #pull day
            self.generate_button = tk.Button(self.window, text="Regenerate", command=self.workout_generator).grid(row=1, column=0)
            self.workout_title = tk.Label(self.window, text="Your Pull Workout:").grid(row=2, column=0) #title
            self.generated_vert_pull1 = tk.Label(self.window, text=self.vert_pull_exercise("vert_pull.txt")+ " 3x8-10").grid(row=3, column=0)
            self.generated_horz_pull1 = tk.Label(self.window, text=self.horz_pull_exercise("horz_pull.txt")+ " 3x10-12").grid(row=4, column=0)
            self.generated_vert_pull2 = tk.Label(self.window, text=self.vert_pull_exercise("vert_pull.txt")+ " 3x12-15").grid(row=5, column=0)
            self.generated_horz_pull2 = tk.Label(self.window, text=self.horz_pull_exercise("horz_pull.txt")+ " 3x12-15").grid(row=6, column=0)
            self.generated_bicep1 = tk.Label(self.window, text=self.bicep_exercise("bicep.txt")+ " 3x8-10").grid(row=7, column=0)
            self.generated_bicep2 = tk.Label(self.window, text=self.bicep_exercise("bicep.txt")+ " 3x12-15").grid(row=8, column=0)
            self.generated_rear_delt2 = tk.Label(self.window, text=self.rear_delt_exercise("rear_delt.txt")+ " 3x15-18").grid(row=9, column=0)

        elif option == 3: #leg day
            self.generate_button = tk.Button(self.window, text="Regenerate", command=self.workout_generator).grid(row=1, column=0)
            self.workout_title = tk.Label(self.window, text="Your Leg Workout:").grid(row=2, column=0)
            self.generated_quad_glute1 = tk.Label(self.window, text=self.quad_glute_exercise("quad_glute.txt")+ " 3x5").grid(row=3, column=0)
            self.generated_quad_glute2 = tk.Label(self.window, text=self.quad_glute_exercise("quad_glute.txt")+ " 3x8-10").grid(row=4, column=0)
            self.generated_hamstring = tk.Label(self.window, text=self.hamstring_exercise("hamstring.txt")+ " 3x10-12").grid(row=5, column=0)
            self.generated_calf = tk.Label(self.window, text=self.calf_exercise("calf.txt")+ " 4x12-15").grid(row=6, column=0)
            self.generated_core1 = tk.Label(self.window, text=self.core_exercise("core.txt")+ " 3 Sets, AMRAP").grid(row=7, column=0)
            self.generated_core2 = tk.Label(self.window, text=self.core_exercise("core.txt")+ " 3 Sets, AMRAP").grid(row=8, column=0)

        elif option == 4: #upper day
            self.generate_button = tk.Button(self.window, text="Regenerate", command=self.workout_generator).grid(row=1, column=0)
            self.workout_title = tk.Label(self.window, text="Your Upper Body Workout:").grid(row=2, column=0)
            self.generated_whole_chest = tk.Label(self.window, text=self.whole_chest_exercise("whole_chest.txt")+ " 4x8-12").grid(row=3, column=0)
            self.generated_whole_back = tk.Label(self.window, text=self.whole_back_exercise("whole_back.txt")+ " 4x8-12").grid(row=4, column=0)
            self.generated_whole_shoulder = tk.Label(self.window, text=self.whole_shoulder_exercise("whole_shoulder.txt")+ " 3x12-15").grid(row=5, column=0)
            self.generated_whole_shoulder = tk.Label(self.window, text=self.whole_shoulder_exercise("whole_shoulder.txt")+ " 3x12-15").grid(row=6, column=0)
            self.generated_tricep = tk.Label(self.window, text=self.tricep_exercise("tricep.txt")+ " 4x10-15").grid(row=7, column=0)
            self.generated_bicep = tk.Label(self.window, text=self.bicep_exercise("bicep.txt")+ " 4x10-15").grid(row=8, column=0)
            
        elif option == 5: #lower day
            self.generate_button = tk.Button(self.window, text="Regenerate", command=self.workout_generator).grid(row=1, column=0)
            self.workout_title = tk.Label(self.window, text="Your Lower Body Workout:").grid(row=2, column=0)
            self.generated_whole_leg1 = tk.Label(self.window, text=self.whole_leg_exercise("whole_leg.txt")+ " 3x5-7").grid(row=3, column=0)
            self.generated_whole_leg2 = tk.Label(self.window, text=self.whole_leg_exercise("whole_leg.txt")+ " 3x8-10").grid(row=4, column=0)
            self.generated_whole_leg3 = tk.Label(self.window, text=self.whole_leg_exercise("whole_leg.txt")+ " 3x10-12").grid(row=5, column=0)
            self.generated_whole_leg4 = tk.Label(self.window, text=self.whole_leg_exercise("whole_leg.txt")+ " 3x12-15").grid(row=6, column=0)
            self.generated_core1 = tk.Label(self.window, text=self.core_exercise("core.txt")+ " 3 Sets, AMRAP").grid(row=7, column=0)
            self.generated_core2 = tk.Label(self.window, text=self.core_exercise("core.txt")+ " 3 Sets, AMRAP").grid(row=8, column=0)

        else: #check of invalid inputs
            self.invalid_input = tk.Label(self.window, text="Invalid input, please input a valid number.").grid(row=2, column=0)

    #random mid chest exercise generator
    def mid_chest_exercise(self, mid_chest_file):
        with open(mid_chest_file, "r") as mid_chest:
            mid_chest_list = []
            for line in mid_chest: #loop through exercises and add to list
                mid_chest_list.append(line.strip("\n"))
            random_mid_chest_exercise = random.randint(0,(len(mid_chest_list)-1)) #get random number based on number of chest exercises in list
        return mid_chest_list[random_mid_chest_exercise]

    #random upper chest exercise generator 
    def upper_chest_exercise(self, upper_chest_file):
        with open(upper_chest_file, "r") as upper_chest:
            upper_chest_list = []
            for line in upper_chest:
                upper_chest_list.append(line.strip("\n"))
            random_upper_chest_exercise = random.randint(0,(len(upper_chest_list)-1))
        return upper_chest_list[random_upper_chest_exercise]

    #random lower chest exercise generator 
    def lower_chest_exercise(self, lower_chest_file):
        with open(lower_chest_file, "r") as lower_chest:
            lower_chest_list = []
            for line in lower_chest:
                lower_chest_list.append(line.strip("\n"))
            random_lower_chest_exercise = random.randint(0,(len(lower_chest_list)-1))
        return lower_chest_list[random_lower_chest_exercise]

    #random whole chest exercise generator 
    def whole_chest_exercise(self, whole_chest_file):
        with open(whole_chest_file, "r") as whole_chest:
            whole_chest_list = []
            for line in whole_chest:
                whole_chest_list.append(line.strip("\n"))
            random_whole_chest_exercise = random.randint(0,(len(whole_chest_list)-1))
        return whole_chest_list[random_whole_chest_exercise]

    #random lateral delt exercise generator      
    def lateral_delt_exercise(self, lateral_delt_file):
        with open(lateral_delt_file, "r") as lateral_delt:
            lateral_delt_list = []
            for line in lateral_delt:
                lateral_delt_list.append(line.strip("\n"))
            random_lateral_delt_exercise = random.randint(0,(len(lateral_delt_list)-1))
        return lateral_delt_list[random_lateral_delt_exercise]

    #random front delt exercise generator      
    def front_delt_exercise(self, front_delt_file):
        with open(front_delt_file, "r") as front_delt:
            front_delt_list = []
            for line in front_delt:
                front_delt_list.append(line.strip("\n"))
            random_front_delt_exercise = random.randint(0,(len(front_delt_list)-1))
        return front_delt_list[random_front_delt_exercise]

    #random rear delt exercise generator      
    def rear_delt_exercise(self, rear_delt_file):
        with open(rear_delt_file, "r") as rear_delt:
            rear_delt_list = []
            for line in rear_delt:
                rear_delt_list.append(line.strip("\n"))
            random_rear_delt_exercise = random.randint(0,(len(rear_delt_list)-1))
        return rear_delt_list[random_rear_delt_exercise]

    #random whole shoulder exercise generator      
    def whole_shoulder_exercise(self, whole_shoulder_file):
        with open(whole_shoulder_file, "r") as whole_shoulder:
            whole_shoulder_list = []
            for line in whole_shoulder:
                whole_shoulder_list.append(line.strip("\n"))
            random_whole_shoulder_exercise = random.randint(0,(len(whole_shoulder_list)-1))
        return whole_shoulder_list[random_whole_shoulder_exercise]

    #random tricep exercise generator            
    def tricep_exercise(self, tricep_file):
        with open(tricep_file, "r") as tricep:
            tricep_list = []
            for line in tricep:
                tricep_list.append(line.strip("\n"))
            random_tricep_exercise = random.randint(0,(len(tricep_list)-1))
        return tricep_list[random_tricep_exercise]

    #random vert pull exercise generator            
    def vert_pull_exercise(self, vert_pull_file):
        with open(vert_pull_file, "r") as vert_pull:
            vert_pull_list = []
            for line in vert_pull:
                vert_pull_list.append(line.strip("\n"))
            random_vert_pull_exercise = random.randint(0,(len(vert_pull_list)-1))
        return vert_pull_list[random_vert_pull_exercise]

    #random horz pull exercise generator            
    def horz_pull_exercise(self, horz_pull_file):
        with open(horz_pull_file, "r") as horz_pull:
            horz_pull_list = []
            for line in horz_pull:
                horz_pull_list.append(line.strip("\n"))
            random_horz_pull_exercise = random.randint(0,(len(horz_pull_list)-1))
        return horz_pull_list[random_horz_pull_exercise]

    #random whole back exercise generator            
    def whole_back_exercise(self, whole_back_file):
        with open(whole_back_file, "r") as whole_back:
            whole_back_list = []
            for line in whole_back:
                whole_back_list.append(line.strip("\n"))
            random_whole_back_exercise = random.randint(0,(len(whole_back_list)-1))
        return whole_back_list[random_whole_back_exercise]

    #random bicep exercise generator            
    def bicep_exercise(self, bicep_file,):
        with open(bicep_file, "r") as bicep:
            bicep_list = []
            for line in bicep:
                bicep_list.append(line.strip("\n"))
            random_bicep_exercise = random.randint(0,(len(bicep_list)-1))
        return bicep_list[random_bicep_exercise]

    #random quad and/or glute exercise generator            
    def quad_glute_exercise(self, quad_glute_file,):
        with open(quad_glute_file, "r") as quad_glute:
            quad_glute_list = []
            for line in quad_glute:
                quad_glute_list.append(line.strip("\n"))
            random_quad_glute_exercise = random.randint(0,(len(quad_glute_list)-1))
        return quad_glute_list[random_quad_glute_exercise]

    #random hamstring exercise generator            
    def hamstring_exercise(self, hamstring_file,):
        with open(hamstring_file, "r") as hamstring:
            hamstring_list = []
            for line in hamstring:
                hamstring_list.append(line.strip("\n"))
            random_hamstring_exercise = random.randint(0,(len(hamstring_list)-1))
        return hamstring_list[random_hamstring_exercise]

    #random calf exercise generator            
    def calf_exercise(self, calf_file,):
        with open(calf_file, "r") as calf:
            calf_list = []
            for line in calf:
                calf_list.append(line.strip("\n"))
            random_calf_exercise = random.randint(0,(len(calf_list)-1))
        return calf_list[random_calf_exercise]

    #random whole leg exercise generator            
    def whole_leg_exercise(self, whole_leg_file,):
        with open(whole_leg_file, "r") as whole_leg:
            whole_leg_list = []
            for line in whole_leg:
                whole_leg_list.append(line.strip("\n"))
            random_whole_leg_exercise = random.randint(0,(len(whole_leg_list)-1))
        return whole_leg_list[random_whole_leg_exercise]
            
    #random core exercise generator            
    def core_exercise(self, core_file,):
        with open(core_file, "r") as core:
            core_list = []
            for line in core:
                core_list.append(line.strip("\n"))
            random_core_exercise = random.randint(0,(len(core_list)-1))
        return core_list[random_core_exercise] 

if __name__ == "__main__":
    workout_GUI()