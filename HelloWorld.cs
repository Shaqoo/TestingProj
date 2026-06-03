// Console.WriteLine("Hello, World!");

// List<string> names = new List<string> { "Alice", "Bob", "Charlie" };
// foreach (var name in names)
// {
//     Console.WriteLine($"Hello, {name}!");
// }
// List<int> numbers = new List<int> { 1, 2, 3, 4, 5 , 6, 7, 8, 9, 10 };

// List<int> nums = [ ..numbers, 11, 12, 13 ];   

// int[] smallerNumbers = numbers[0..5].ToArray(); 
// Console.WriteLine("Numbers: " + string.Join(", ", numbers));


// int[] largerNums = numbers[5..].ToArray(); 
// Console.WriteLine("Numbers: " + string.Join(", ", nums));
// Console.WriteLine("Smaller Numbers: " + string.Join(", ", smallerNumbers));
// Console.WriteLine("Larger Numbers: " + string.Join(", ", largerNums));

// string name = "Ade";
// name.ToUpper();

SortedSet<int> ints = new SortedSet<int>([1,2,3,2,3,4,4,2,4,5,6,3,4,2,1]);

Console.WriteLine(string.Join(", ",ints));
Console.WriteLine(string.Join(", ",ints.Union([2,4,5,8,44,33,23])));