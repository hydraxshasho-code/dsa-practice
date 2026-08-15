import math as m
def calculator():
    while True:
            print("""1. Addition
                2. Subtraction
                3. Multiplication
                4. Division
                5. Square Root
                6. Exponentiation
                7. Sine
                8. Cosine
                9. Tangent
                10. Logarithm
                11. Factorial
                12. Modulo
                13. Absolute Value
                14. Floor Division
                15. Power
                16. Rounding
                17. Permutations
                18. Combinations
                19. Hyperbolic Sine
                20. Hyperbolic Cosine
                21. Hyperbolic Tangent
                22. Inverse Sine
                23. Inverse Cosine
                24. Inverse Tangent
                25. Natural Logarithm
                26. Logarithm Base 10
                27. Logarithm Base 2
                28. Greatest Common Divisor
                29. Least Common Multiple
                30. Degrees to Radians
                31. Radians to Degrees
                32. Sine Hyperbolic
                33. Cosine Hyperbolic
                34. Tangent Hyperbolic
                0. Exit""")
            choice = input("Enter your choice (0-34): ")
            if choice == '0':
                print("Exiting the calculator. Goodbye!")
                break
            elif choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34']:
                if choice in ['1', '2', '3', '4', '6', '12', '14', '15']:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                elif choice in ['5', '11']:
                    num1 = float(input("Enter the number: "))
                elif choice in ['7', '8', '9', '19', '20', '21']:
                    angle = float(input("Enter the angle in degrees: "))
                    num1 = m.radians(angle)
                elif choice in ['22', '23', '24']:
                    num1 = float(input("Enter the value: "))
                elif choice in ['25', '26', '27']:
                    num1 = float(input("Enter the number: "))
                elif choice in ['28', '29']:
                    num1 = int(input("Enter the first integer: "))
                    num2 = int(input("Enter the second integer: "))
                elif choice in ['30']:
                    degrees = float(input("Enter the angle in degrees: "))
                    print(f"{degrees} degrees is equal to {m.radians(degrees)} radians.")
                    continue
                elif choice in ['31']:
                    radians = float(input("Enter the angle in radians: "))
                    print(f"{radians} radians is equal to {m.degrees(radians)} degrees.")
                    continue
                elif choice in ['32', '33', '34']:
                    angle = float(input("Enter the angle in degrees: "))
                    num1 = m.radians(angle)
                
                if choice == '1':
                    result = num1 + num2
                elif choice == '2':
                    result = num1 - num2
                elif choice == '3':
                    result = num1 * num2
                elif choice == '4':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        print("Error: Division by zero is not allowed.")
                        continue
                elif choice == '5':
                    result = m.sqrt(num1)
                elif choice == '6':
                    result = m.pow(num1, num2)
                elif choice == '7':
                    result = m.sin(num1)
                elif choice == '8':
                    result = m.cos(num1)
                elif choice == '9':
                    result = m.tan(num1)
                elif choice == '10':
                    result = m.log(num1)
                elif choice == '11':
                    result = m.factorial(int(num1))
                elif choice == '12':
                    result = num1 % num2
                elif choice == '13':
                    result = abs(num1)
                elif choice == '14':
                    result = num1 // num2
                elif choice == '15':
                    result = pow(num1, num2)
                elif choice == '16':
                    result = round(num1)
                elif choice == '17':
                    result = m.perm(int(num1), int(num2))
                elif choice == '18':
                    result = m.comb(int(num1), int(num2))
                elif choice == '19':
                    result = m.sinh(num1)
                elif choice == '20':
                    result = m.cosh(num1)
                elif choice == '21':
                    result = m.tanh(num1)
                elif choice == '22':
                    result = m.asin(num1)
                elif choice == '23':
                    result = m.acos(num1)
                elif choice == '24':
                    result = m.atan(num1)
                elif choice == '25':
                    result = m.log(num1)
                elif choice == '26':
                    result = m.log10(num1)
                elif choice == '27':
                    result = m.log2(num1)
                elif choice == '28':
                    result = m.gcd(num1, num2)
                elif choice == '29':
                    result = (num1 * num2) // m.gcd(num1, num2)
                elif choice == '32':
                    result = m.sinh(num1)
                elif choice == '33':
                    result = m.cosh(num1)
                elif choice == '34':
                    result = m.tanh(num1)
                print(f"The result is: {result}")
            else:
                print("Invalid choice. Please enter a number between 0 and 34.")
if __name__ == "__main__":
    calculator()


