// https://adventofcode.com/2015/day/1

fn main() {
    let raw_data = include_str!("input.txt");

    let result = raw_data
        .chars()
        .map(|x| (x == '(') as i32 * 2 - 1)
        .sum::<i32>();

    println!("{}", result);
}
