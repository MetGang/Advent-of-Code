// https://adventofcode.com/2015/day/1

fn main() {
    let raw_data = include_str!("input.txt");

    let result = 1 + raw_data
        .chars()
        .map(|x| (x == '(') as i32 * 2 - 1)
        .scan(0, |acc, x| { *acc += x; Some(*acc) })
        .position(|x| x == -1)
        .unwrap();

    println!("{:?}", result);
}
