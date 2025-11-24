import numpy as np

def bytes_to_image(byte_data, width, height):
      return 

def serialize_commands(commands, space, rt):
        """
        Serialize  goal pose command and gripper command into string format.
        space: 'JS' for joint space or 'TS' for task space
        commands: list of floats representing the command values
        rt: True for real-time, False for non-real-time
        """
        command_string = f"{space} {rt} "
        for i in commands:
            command_string += f"{i:.4f} "
        command_string = command_string.strip() + "\n"   

        return command_string

def parse_states(state_string):
        """
        Parse the state string received from the Colossus arm into a dictionary.
        """

        state_values = list(map(float, state_string.strip().split()))
        
        state_array = np.array([state_values[0:5], state_values[6:11]]) 
         
        return 