age = 32
print("My age is {0} years".format(age))

# example where whe are going to store integer and strigs in to index numbers in memory using {} for number of index
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format
      (31, "Jan", "Mar,", "May", "Jul", "Aug", "Oct", "Dec"))

# same result here
print("There are {0} days in  Jan, Mar, May, Jul, Aug, Oct, and Dec".format(31))

# !!! Numbers in curly-brackets determine which of the offered values are going to be used.

print("Jan: {2}, Feb: {0}, March: {2}, April: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}."
      .format(28, 30, 31))

# Example of how you can use 3 different integer values and add them to your list of values, and then insert in strings

print()

print("""Jan: {2},
 Feb: {0},
 Mar: {2},
 Apr: {1},
 May: {2},
 Jun: {1},
 Jul: {2},
 Sep: {1},
 Oct: {2},
 Nov: {1},
 Dec: {2}""".format(28, 30, 31))
