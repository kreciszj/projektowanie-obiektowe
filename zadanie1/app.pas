
Program app;

procedure GenerateRandomNumbers(var arr: array of integer);
var
  i: integer;
begin
  randomize;
  for i := Low(arr) to High(arr) do
  begin
    arr[i] := random(101);
  end;
end;

procedure BubbleSort(var arr: array of integer);
var
  i, j, temp: integer;
begin
  for i := Low(arr) to High(arr) do
  begin
    for j := Low(arr) to High(arr) - 1 do
    begin
      if arr[j] > arr[j+1] then
      begin
        temp := arr[j];
        arr[j] := arr[j+1];
        arr[j+1] := temp;
      end;
    end;
  end;
end;

var
  numbers: array[1..50] of integer;
  i: integer;
begin
  GenerateRandomNumbers(numbers);

  writeln('Unsorted numbers:');
  for i := 1 to 50 do
    write(numbers[i], ' ');
  writeln;

  BubbleSort(numbers);

  writeln('Sorted numbers:');
  for i := 1 to 50 do
    write(numbers[i], ' ');
  writeln;
end.