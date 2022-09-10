// https://adventofcode.com/2021/day/1

fn main() {
    let raw_data = include_str!("input.txt");

    let result = raw_data
        .lines()
        .map(|x| x.parse::<u16>().unwrap())
        .collect::<Vec<u16>>()
        .windows(2)
        .filter(|x| x.first() < x.last())
        .count();

    println!("{}", result);
}
