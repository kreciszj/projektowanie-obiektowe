program app;

const
  MAX_SIZE = 1024;

procedure GenerateRandomNumbers(var arr: array of integer; fromVal, toVal, count: integer);
var
  i: integer;
begin
  randomize;
  for i := 1 to count do
  begin
    arr[i] := fromVal + random(toVal - fromVal + 1);
  end;
end;

procedure BubbleSort(var arr: array of integer; count: integer);
var
  i, j, temp: integer;
begin
  for i := 1 to count - 1 do
  begin
    for j := 1 to count - i do
    begin
      if arr[j] > arr[j + 1] then
      begin
        temp := arr[j];
        arr[j] := arr[j + 1];
        arr[j + 1] := temp;
      end;
    end;
  end;
end;

function IsSorted(var arr: array of integer; count: integer): boolean;
var
  i: integer;
begin
  IsSorted := true;
  for i := 1 to count - 1 do
  begin
    if arr[i] > arr[i + 1] then
    begin
      IsSorted := false;
      exit;
    end;
  end;
end;

function InRange(value, minVal, maxVal: integer): boolean;
begin
  InRange := (value >= minVal) and (value <= maxVal);
end;

procedure RunTests;
var
  testArr: array[1..MAX_SIZE] of integer;
  i: integer;
  allInRange: boolean;
  sumOfValues: integer;
begin
  writeln('--- Running Tests ---');

  { Test 1: Generate 50 random numbers in [0..100], check if all are in range }
  for i := 1 to MAX_SIZE do
    testArr[i] := 0;
  GenerateRandomNumbers(testArr, 0, 100, 50);
  allInRange := true;
  for i := 1 to 50 do
    if not InRange(testArr[i], 0, 100) then
      allInRange := false;

  if allInRange then
    writeln('Test 1: Passed')
  else
    writeln('Test 1: Failed (numbers out of [0..100] range)');

  { Test 2: Generate 5 random numbers in [1..5], sort them, check if sorted }
  for i := 1 to MAX_SIZE do
    testArr[i] := 0;
  GenerateRandomNumbers(testArr, 1, 5, 5);
  BubbleSort(testArr, 5);
  if IsSorted(testArr, 5) then
    writeln('Test 2: Passed')
  else
    writeln('Test 2: Failed (the array is not sorted correctly)');


  { Test 3: Generate 10 numbers in [10..20], sort them, check if sorted }
  for i := 1 to MAX_SIZE do
    testArr[i] := 0;
  GenerateRandomNumbers(testArr, 10, 20, 10);
  BubbleSort(testArr, 10);
  if IsSorted(testArr, 10) then
    writeln('Test 3: Passed')
  else
    writeln('Test 3: Failed (the array is not sorted)');

  { Test 4: Generate 5 numbers in [0..5], check if their sum is in [0..25] }
  for i := 1 to MAX_SIZE do
    testArr[i] := 0;
  GenerateRandomNumbers(testArr, 0, 5, 5);
  
  sumOfValues := 0;
  for i := 1 to 5 do
    sumOfValues := sumOfValues + testArr[i];

  if (sumOfValues >= 0) and (sumOfValues <= 25) then
    writeln('Test 4: Passed')
  else
    writeln('Test 4: Failed (sum out of range [0..25])');

  { Test 5: Generate 0 elements, just to ensure no crash }
  for i := 1 to MAX_SIZE do
    testArr[i] := 0;
  GenerateRandomNumbers(testArr, 1, 5, 0);
  BubbleSort(testArr, 0);
  writeln('Test 5: Passed');

  writeln('--- Tests Completed ---');
end;

var
  i: integer;
  fromVal: integer = 0;
  toVal: integer = 100;
  count: integer = 65;
  numbers: array[1..MAX_SIZE] of integer;
begin
  RunTests;
  writeln;
  writeln('Generate ', count, ' random numbers in the range [', fromVal, '..', toVal, ']...');
  GenerateRandomNumbers(numbers, fromVal, toVal, count);

  writeln('Unsorted numbers:');
  for i := 1 to count do
    write(numbers[i], ' ');
  writeln;

  BubbleSort(numbers, count);

  writeln('Sorted numbers:');
  for i := 1 to count do
    write(numbers[i], ' ');
  writeln;
end.
