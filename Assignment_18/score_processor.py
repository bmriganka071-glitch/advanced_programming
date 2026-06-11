# score_processor.py

class ScoreProcessor:
    def process_score_file(self, file_path: str) -> int:
        file = None
        try:
            # The Safe Zone
            file = open(file_path, "r")
            content = file.read()
            numeric_value = int(content)
            final_score = numeric_value * 10
            
        except FileNotFoundError:
            # Custom message for missing file
            print(f"Error: The file '{file_path}' does not exist.")
            raise  
            
        except ValueError:
            # Custom message for bad data format
            print(f"Error: The data in '{file_path}' is not a valid number.")
            raise  
            
        else:
            # Runs only on total success
            print("Data processed successfully")
            return final_score
            
        finally:
            # Guaranteed to clean up resources under all conditions
            print("File cleanup completed")
            if file is not None:
                file.close()