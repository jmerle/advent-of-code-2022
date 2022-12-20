import sys
from dataclasses import dataclass

@dataclass
class Number:
    value: int
    original_idx: int
    mixed: int

def main() -> None:
    data = sys.stdin.read().strip()

    nums = [Number(int(value) * 811589153, i, 0) for i, value in enumerate(data.splitlines())]

    for i in range(10):
        for _ in range(len(nums)):
            idx_to_mix = min([j for j in range(len(nums)) if nums[j].mixed == i], key=lambda i: nums[i].original_idx)
            num_to_mix = nums[idx_to_mix]

            new_idx = (idx_to_mix + num_to_mix.value) % (len(nums) - 1)

            nums.remove(num_to_mix)
            nums.insert(new_idx, num_to_mix)

            num_to_mix.mixed += 1

    zero_idx = next(i for i, num in enumerate(nums) if num.value == 0)
    print(sum(nums[(zero_idx + i) % len(nums)].value for i in [1000, 2000, 3000]))

if __name__ == "__main__":
    main()
