#consider a scenario where students are waiting in a queue at a university's student dining hall. implement a python code that simulates a queue data structure for managing the student queue
#design a class named studentqueue with methods to enqueue students joining the queue, dequeue students being served, check if the queue is empty and determine the current size of the queue
#provide an example (with output) usage of your implemented class ,demontrating how students join the queue, get served, and how to acertain the size of the queue


class StudentQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, student):
        """Add a student to the end of the queue."""
        self.queue.append(student)

    def dequeue(self):
        """Remove and return the student at the front of the queue."""
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty. No student to dequeue.")
            return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the current size of the queue."""
        return len(self.queue)

# Usage:
if __name__ == "__main__":
    # Create a student queue
    student_queue = StudentQueue()

    # Enqueue students
    student_queue.enqueue("Student1")
    student_queue.enqueue("Student2")
    student_queue.enqueue("Student3")

    # Check the size of the queue
    print(f"Queue size: {student_queue.size()}")  # Output: Queue size: 3

    # Dequeue a student 
    served_student = student_queue.dequeue()
    if served_student:
        print(f"Served student: {served_student}")  # Output: Served student: Student1

    # Check if the queue is empty
    print(f"Is the queue empty? {student_queue.is_empty()}")  # Output: Is the queue empty? False

    # Check the size of the queue after serving
    print(f"Queue size after serving: {student_queue.size()}")  # Output: Queue size after serving: 2


























