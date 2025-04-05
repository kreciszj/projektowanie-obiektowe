
Program app;

procedure GenerateRandomNumbers;
var
  i: integer;
begin
  randomize;
  for i := 1 to 50 do
  begin
    writeln('Random number ', i, ': ', random(101));
  end;
end;

begin
  writeln('Generating 50 random numbers from 0 to 100...');
  GenerateRandomNumbers;
end.