largest = None
smallest = None

while True:
    try:
        num_as_string = raw_input("Enter a number: ")
        num_value = int(num_as_string)

        if largest is None or num_value > largest:
            largest = num_value

        if smallest is None or num_value < smallest:
            smallest = num_value

    except:
        if num_as_string == "done":
            break
        else:
            print "Invalid input"
            continue

print "Maximum is", largest
print "Minimum is", smallest