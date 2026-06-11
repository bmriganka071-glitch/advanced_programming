# test_score_processor.py

import pytest
import os
from score_processor import ScoreProcessor

class TestScoreProcessor:
    
    def test_successful_calculation(self):
        """
        Happy Path Test: Ensures a valid file with an integer 
        correctly scales the score by a factor of 10.
        """
        # Setup: Create a temporary test file
        test_filename = "temp_valid_score.txt"
        with open(test_filename, "w") as f:
            f.write("8")  # 8 * 10 should equal 80
            
        processor = ScoreProcessor()
        
        try:
            # Execution
            result = processor.process_score_file(test_filename)
            
            # Assertion: Verify the mathematical output matches expectations
            assert result == 80
            
        finally:
            # Teardown: Clean up the physical file from your storage disk
            if os.path.exists(test_filename):
                os.remove(test_filename)

    def test_missing_file_handling(self):
        """
        Error Path Test: Assures the processor correctly handles 
        and propagates a FileNotFoundError when targeted with a ghost path.
        """
        processor = ScoreProcessor()
        ghost_path = "non_existent_file_xyz.txt"
        
        # pytest.raises acts like an interception glove. 
        # The test PASSES only if the block inside raises a FileNotFoundError.
        with pytest.raises(FileNotFoundError):
            processor.process_score_file(ghost_path)