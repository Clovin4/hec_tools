"""Main module."""
import os
# if __package__ is None or __package__ == '':
#     import HMScompute
# else:
#     from . import HMScompute


class HMS:
    def __init__(self, loc, prompt=True, run=None) -> None:
        self.loc = loc
        self.run = run
        self._check_hms()
        self.prjName = self.get_hms_prjName()
        if prompt:
            self.run_name = self.get_run_names()
        else:
            self.run_name = self.get_run_names()

    def _check_hms(self):
        """Check if HMS is installed."""
        if not os.path.exists(self.loc):
            raise FileNotFoundError(f"HMS not found at {self.loc}")
        
    def get_hms_prjName(self):
        """Get project info."""
        loc = self.loc
        # return file path to the .hms file loc+"\\*.hms"
        hms_file = [os.path.join(loc, f) for f in os.listdir(loc) if f.endswith(".hms")][0]

        # read the .hms file and return the contents
        with open(hms_file, "r") as f:
            hms_file = f.read()

        project_name = hms_file.split("\n")[0].split("=")[-1].strip().split(" ")[-1]

        return project_name
    
    def get_run_names(self):

        loc = self.loc
        run = self.run
        # return file path to the .hms file loc+"\\*.run"
        run_file = [os.path.join(loc, f) for f in os.listdir(loc) if f.endswith(".run")][0]

        # read the .hms file and return the contents
        with open(run_file, "r") as f:
            run_file = f.read()

        run_file = run_file.split("\n")

        run_names = [r.split("=")[-1].strip() for r in run_file if r.startswith("Run")]

        # assign the run names to a dictionary for selection by number
        run_names = {i+1:run_names[i] for i in range(len(run_names))}

        # if the run name is not specified, prompt the user to select one
        if run is None:
            print("Select a run:")
            for k, v in run_names.items():
                print(f"{k}: {v}")
            run = int(input("Enter the number of the run you want to use: "))
            run = run_names[run]
        else:
            if run not in run_names.values():
                raise ValueError(f"Run name {run} not found in {run_names.values()}")
        return run
    
    def get_bat_loc(self):
        """Get the location of the .bat file.
        The bat file is in this directory:"""
        bat_loc = r'hec_tools\HMScompute.bat'
        # check if the .bat file exists
        if not os.path.exists(bat_loc):
            raise FileNotFoundError(f"Could not find the .bat file at {bat_loc}")
        return bat_loc
    
    def get_hms_loc(self):
        return self.loc

    def count_files(self, ext):
        """Count the number of files with the specified extension."""
        loc = self.loc
        files = [f for f in os.listdir(loc) if f.endswith(ext)]
        return len(files)