#add import


from question_b.question_b import get_user_numbers










def display_user_numbers(numbers):

            low = min(numbers)
            high = max(numbers)
            total = sum(numbers)
            average = total / len(numbers)


            print("\nuser_numbers:")
            print(f"Low number: {low}")
            print(f"High number: {high}")
            print(f"total: {total}")
            print(f"average: {average}")
