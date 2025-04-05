program app;

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

var
  i: integer;
  fromVal: integer = 0;
  toVal: integer = 100;
  count: integer = 65;
  numbers: array[1..65] of integer;

begin
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
