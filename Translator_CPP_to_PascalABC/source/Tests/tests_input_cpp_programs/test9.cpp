function fun1(n : integer): integer;
begin
    var b : integer := n+2;
    var r : integer := 0;
    b := b*2;
    if (b<10) then
        begin
            r := b-4;
        end
    else
        begin
            if (b>20) then
                begin
                    r := b*b;
                end
            else
                begin
                    r := 2;
                end;
        end;
    Result := r;
end;

begin
    var a : integer := 3;
    var res : integer := 0;
    res := fun1(a);
    writeln(res)
end.