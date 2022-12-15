
def count_batteries_by_usage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")
  for i in range(0,7):
    if count<310:
      print("low")
    elif count>=310 and count<=929:
      print("medium")
     else:
      print("high")
  


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
