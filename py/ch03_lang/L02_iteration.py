def main():

    # print("Python iteration demo")
    # while True:

    #     name = input("What is your name? ")
    #     if not name:
    #         break
    
    #     print(f"Nice to meet you, {name}!")

    nums = [1, 5, 10, 7, 2]
    for num in nums:
        print(f"The next number is {num}")

    for idx, num in enumerate(nums, start=1):
        print(f"Index {idx} has value {num}")



if __name__ == "__main__":
    main()