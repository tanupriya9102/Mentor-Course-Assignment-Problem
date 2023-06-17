def solve_mentor_subject_assignment(effectiveness_matrix):
    num_mentors = len(effectiveness_matrix)
    num_subjects = len(effectiveness_matrix[0])

    # Create a matrix of differences by subtracting the effectiveness scores from the maximum score
    max_score = max(max(row) for row in effectiveness_matrix)
    diff_matrix = [[max_score - score for score in row] for row in effectiveness_matrix]

    # Initialize arrays to keep track of assigned mentors and subjects
    assigned_mentors = [-1] * num_mentors
    assigned_subjects = [False] * num_subjects

    # Perform the assignment process
    for _ in range(num_mentors):
        mentor = -1

        # Find an unassigned mentor
        for i in range(num_mentors):
            if assigned_mentors[i] == -1:
                mentor = i
                break

        # Find an unassigned subject with the maximum difference for the mentor
        max_diff = -1
        subject = -1
        for j in range(num_subjects):
            if not assigned_subjects[j] and diff_matrix[mentor][j] > max_diff:
                max_diff = diff_matrix[mentor][j]
                subject = j

        # Assign the mentor to the subject
        assigned_mentors[mentor] = subject
        assigned_subjects[subject] = True

    # Return the assignments
    return [(mentor + 1, subject + 1) for mentor, subject in enumerate(assigned_mentors)]

# Example usage
if __name__ == '__main__':
    # Define the effectiveness matrix
    effectiveness_matrix = [
        [85, 75, 90, 80, 70, 85],
        [90, 80, 85, 75, 80, 80],
        [80, 90, 70, 85, 90, 70],
        [75, 85, 80, 90, 85, 75],
        [70, 70, 75, 80, 75, 30]
    ]
       1      2      3        4  5   6
'''    	Math English Science SST Art PE
  M1    85	   75	  90	 80	 70	 85
  M2    90	   80	  85	 75  80  80
  M3    80	   90	  70	 85	 90	 70
  M4    75	   85	  80	 90	 85	 75
  M5    70	   70	  75	 80	 75	 30'''


    # Solve the mentor-subject assignment problem
    assignments = solve_mentor_subject_assignment(effectiveness_matrix)

    # Print the assignments
    for mentor, subject in assignments:
        print(f"Mentor {mentor} is assigned to Subject {subject}")
