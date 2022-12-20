import sys
from dataclasses import dataclass

@dataclass
class Number:
    value: int
    original_idx: int
    mixed: bool

def main() -> None:
    data = sys.stdin.read().strip()

    nums = [Number(int(value), i, False) for i, value in enumerate(data.splitlines())]

    for _ in range(len(nums)):
        idx_to_mix = min([i for i in range(len(nums)) if not nums[i].mixed], key=lambda i: nums[i].original_idx)
        num_to_mix = nums[idx_to_mix]

        new_idx = (idx_to_mix + num_to_mix.value) % (len(nums) - 1)

        nums.remove(num_to_mix)
        nums.insert(new_idx, num_to_mix)

        num_to_mix.mixed = True

    zero_idx = next(i for i, num in enumerate(nums) if num.value == 0)
    print(sum(nums[(zero_idx + i) % len(nums)].value for i in [1000, 2000, 3000]))

if __name__ == "__main__":
    main()
