import unittest
from TestUtils import TestParser
class ParserSuite(unittest.TestCase):
    def test_01(self):
        """More complex program"""
        input = """
        Function checkSymmetric (A:array[0 .. 10] of REAL; N:Integer ) : Boolean;
                Var Flag:Boolean;
                    i :Integer;
                Begin
                Flag:=True;
                For  i :=1 to N do
                If(A[i] <> A[N-i  +1]) Then
                Flag :=False;       { Cham dut kiem tra, ket qua qua trinh : khong doi xung }
                return flag;
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_02(self):
        input = """
        function max(num1, num2: integer): integer;

        var
        (* local variable declaration *)
        result: integer;
        
        begin
        if (num1 > num2) then
            result := num1;
        
        else
            result := num2;
            max := result;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_03(self):
        input = """var a: array[2 .. 10] of real;
            b,c: integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    
    def test_04(self):
        input = """
                var
            a, b, ret : integer;
        (*function definition *)
        function max(num1, num2: integer): integer;
        var
           (* local variable declaration *)
            result: integer;
        begin
            if (num1 > num2) then
            result := num1;
            else
            result := num2;
            max := result;
        end
        begin
        end
        """
        expect = "Error on line 16 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_05(self):
        input = """
                var
        a, b, c,  min: integer;
        procedure findMin(x, y, z: integer; m: integer); 
        (* Finds the minimum of the 3 values *)
        
        begin
            check: boolean;
            if x < y then
            m:= x;
            else
            m:= y;
        
            if z < m then
            m:= z;
        end { end of procedure findMin }  
        
        procedure main();
        begin
            writeln(" Enter three numbers: ");
            readln( a, b, c);
            findMin(a, b, c, min); (* Procedure call *)
        
            writeln(" Minimum: ", min);
        end
        """
        expect = "Error on line 8 col 17: :"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_06(self):
        input = """
                var
            a, b : integer;
        (*procedure definition *)
        procedure swap(x, y: integer); 

        var
            temp: integer;

        begin
            temp := x;
            x:= y;
            y := temp;
        end

        procedure main();
        begin
            a := 100;
            b := 200;
            writeln("Before swap, value of a : ", a );
            writeln("Before swap, value of b : ", b );

            (* calling the procedure swap  by value   *)
            swap(a, b);
            writeln("After swap, value of a : ", a );
            writeln("After swap, value of b : ", b );
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))


    def test_07(self):
        input = """
        A:array[0 .. 10] of REAL
        """
        expect = "Error on line 2 col 8: A"
        self.assertTrue(TestParser.test(input,expect,207))
    
    def test_08(self):
        input = """
        fun()[69]:array[0 .. 10] of REAL
        """
        expect = "Error on line 2 col 8: fun"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_09(self):
        input = """
        VAR Hours, Pay: INTEGER;
        PROCEDURE main();
        """
        expect = "Error on line 4 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_10(self):
        input = """
        var
            greetings: string;
            name: array [1 .. 10] of integer;
            organisation: string;

        procedure main();
        begin
            greetings := "Hello ";
            message := "Good Day!";

            writeln("Please Enter your Name");
            readln(name);
        with
            writeln("Please Enter the name of your Organisation");
            readln(organisation);

            writeln(greetings, name, " from ", organisation);
            writeln(message); 
        end
        """
        expect = "Error on line 15 col 19: ("
        self.assertTrue(TestParser.test(input,expect,210))

    def test_11(self):
        input = """
        var
        a, b, c: integer;
        procedure display();
        var
        """
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_12(self):
        input = """
                var
        a, b, c: integer;
        procedure display();
        var
        x, y, z: integer;
        """
        expect = "Error on line 7 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_13(self):
        input = """
        procedure swap(x, y: integer); 
        var
            temp: integer;
        beGin
        var A:array[0-100 .. a-10] of REAL;
        begin
            temp := x;
            x:= y;
            y := temp;
        end
        end
        """
        expect = "Error on line 6 col 8: var"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_14(self):
        input = """
        Procedure Array1D(A : array[0 .. 10] of integer;N:Integer);
                Var i: Integer;
                Begin
                Write("N=");
                Readln( N);
                For i:=0 to N do
                    Begin
                        Write("N[", i,"]= ");
                        Readln( A[i] );
                    End
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_15(self):
        input = """
        function statement(c: real): integer;
        BEGIN
            if()
            then
            statement(3,a+1,a<>1,a[1]);
            return 1;
            else
            return;
        END
        """
        expect = "Error on line 4 col 15: )"
        self.assertTrue(TestParser.test(input,expect,215))

    
    def test_16(self):
        input = """
        Procedure Array1D(A : array[0 .. 10] of integer;N:Integer);
        begin
        Procedure Sum(a, c:Real);
        begin
        end
        end
        """
        expect = "Error on line 4 col 8: Procedure"
        self.assertTrue(TestParser.test(input,expect,216))

    
    def test_17(self):
        input = """
        Var
            S : String;
            i : Real;

        Procedure main();
        Begin
            i := -0.563;
            Str(i, S);
            Write(S);
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    
    def test_18(self):
        input = """
        Function GetSize() : Integer;
        Begin
        GetSize := topPointer;
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    
    def test_19(self):
        input = """
        
        Var Ch : String;

        Procedure main();
        Begin
        Writeln("Press \\"\\"q\\"\\" to exit...");
        Ch := Readkey();
        While Ch <> "q" do
        Begin
            Writeln("Please press \\"\\"q\\"\\" to exit.");
            Ch := Readkey();
        End
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    
    def test_20(self):
        input = """
        procedure main();
        begin
            writeln("Please enter your first name: ");
            readln(firstname);

            writeln("Please enter your surname: ");
            readln(surname);
            /""''""
            writeln();
            writeln(message, " ", firstname, " ", surname);
        end
        """
        expect = "Error on line 9 col 12: /"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_21(self):
        input = """
        EOF
        """
        expect = "Error on line 2 col 8: EOF"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_22(self):
        input = """
        procedure main();
        begin
            a:= 10;
            (* check the boolean condition using if statement *)

            if( a < 20 ) then
            (* if condition is true then print the following *)
            writeln("a is less than 20 " );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    
    def test_23(self):
        input = """
        VAR Pennies:  INTEGER;
        Tendered, Cost,  Remainder: REAL;
        PROCEDURE Main();
        BEGIN
        (* Input  necessary information *)
        Write("Enter cost  of item: ");
        Read(Cost);
        Write("Enter  amount tendered: ");
        Read(Tendered);
        (* Compute the  change in pennies *)
        Remainder :=  Tendered - Cost;
        Pennies := 0;
        WHILE Remainder  > 0 DO BEGIN
        Remainder :=  Remainder - 0.01;
        Pennies :=  Pennies + 1;
        END (* WHILE *)
        (* Output all  required Results *)
        Write("Cost is:  ");
        Write(Cost);
        Write(" Amount  tendered is: ");
        Write(Tendered);
        Write(" Change  is: ");
        WriteLn(Pennies);
        END (*  BadChanger *)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_24(self):
        input = """
        var i: integer ;
                function f(): integer ;
                begin
                    return 200;
                end
                procedure main() ;
                var
                    main: integer ;
                begin
                    main := f() ;
                    putIntLn(main);
                    with
                        i: integer;
                        main: integer;
                        f: integer;
                    do begin
                        main := f := i:= 100;
                        putIntLn (i);
                        putIntLn (main );
                        putIntLn (f);
                    end
                    putIntLn (main);
                end
                var g: real ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_25(self):
        input = """
        procedure main();
        begin
            writeln("27e1615212f3c6ea846ed6c412df1361ce97f006ee20bb5aa2483a3b61d5cadd");
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_26(self):
        input = """
        var
        a: integer;

        procedure main();
        begin
            for a := 10  to 20 do
                b: integer;
            begin
                writeln("value of a: ", a);
            end
        end
        """
        expect = "Error on line 8 col 17: :"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_27(self):
        input = """
        var
            a: integer;

        procedure main();
        begin
            a := := 10;
            while  a < 20  do

            begin
                writeln("value of a: ", a);
                a := a + 1;
            end
        end
        """
        expect = "Error on line 7 col 17: :="
        self.assertTrue(TestParser.test(input,expect,227))

    def test_28(self):
        input = """
        pROCEDURE foo(c: real) ;
            BEGIN
                with a , b : integer ; c : array [1 .. 2] of real;
            END
        """
        expect = "Error on line 5 col 12: END"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_29(self):
        input = """
        pROCEDURE foo(c: real) ;
            BEGIN
            with a , b : integer ; c : array [1 .. 2] of real ;
            d := c [a] + b ;
            END
        """
        expect = "Error on line 5 col 14: :="
        self.assertTrue(TestParser.test(input,expect,229))

    def test_30(self):
        input = """
        var x:real ;
            BEGIN
                whILe(a<>1) do beGin
                    if(a=1) then;
                    foo();
                end
            END
        """
        expect = "Error on line 3 col 12: BEGIN"
        self.assertTrue(TestParser.test(input,expect,230))


    def test_31(self):
        input = """
        FUNcTION foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                var x,y: real ;
                END
                BEGIN
        """
        expect = "Error on line 4 col 16: END"
        self.assertTrue(TestParser.test(input,expect,231))


    def test_32(self):
        input = """
        proceDure Hello(a, b:integer);
                begin
                    a := b + c;
                    writeln("Hello, world!");
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_33(self):
        input = """
        var
        a: integer;

        procedure main();
begin
    a := 10;
   (* while loop execution *)
    while  a < 20 do

    begin
        writeln("value of a: ", a);
        a:=a +1;

        if( a > 15) then
         (* terminate the loop using break statement *)
    break;
    end
        """
        expect = "Error on line 19 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,233))

    def test_34(self):
        input = """
        Var 
        S1, S2 : String;

        Procedure main();
        Begin
        S1 := "Hey!";
        S2 := " How are you?";
        Write(S1 + S2); { "Hey! How are you?" }
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_35(self):
        input = """
        Var 
        S1, S2, S3 : String;

        Procedure main();
        Begin
        S1 := "Woaw!";
        S2 := " Viet ";
        S3 := " is such a handsome man!";
        Write(S1 + S2 + S3); { "Woaw! Viet is such a handsome man!" }
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))

    def test_36(self):
        input = """
        Procedure Main();
        Begin
            While 1 do
            Begin
                myIntArray[i] := 1;
                myBoolArray[i] := True;
            End
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))

    def test_37(self):
        input = """
        var
            a, b, c: integer;
        procedure display();

        var
            a, b, c: integer;
        """
        expect = "Error on line 8 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,237))

    def test_38(self):
        input = """
        writeln("Winthin the procedure display");
        writeln("Winthin the procedure display");
        writeln("Winthin the procedure display");
        """
        expect = "Error on line 2 col 8: writeln"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_39(self):
        input = """
        procedure main();
        begin
            a:= 10;
            (* check the boolean condition using if statement *)

            if( a < 20 ) then
              (* if condition is true then print the following *) 
                writeln("a is less than 20 " );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))

    def test_40(self):
        input = """
        procedure main();
        begin
            a := 10;
            (* while loop execution *)
            while  a < 20 do

            begin
                writeln("value of a: ", a);
                a:=a +1;

                if( a > 15) then
                 (* terminate the loop using break statement *)
                break;
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_41(self):
        input = """
        procedure main();
        begin
            a := 100;
            (* check the boolean condition *)
            if( a < 20 ) then
              (* if condition is true then print the following *)
            writeln("a is less than 20" );

            else
              (* if condition is false then print the following *) 
            writeln("a is not less than 20" );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_42(self):
        input = """
        begin
        if (num1 > num2) then
            result := num1;

        else
            result := num2;
        max := result;
        end

        begin
            a := 100;
            b := 200;
           (* calling a function to get max value *)
            ret := max(a, b);

            writeln( "Max value is : ", ret );
        end
        """
        expect = "Error on line 2 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_43(self):
        input = """
        proceDure Hello(a, b:integer);
                begin
                    writeln("Hello, world!");
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_44(self):
        input = """
        procedure main((()) ;
                beGin
                if a=b then if c = d then e := f;
                else i := 1;
                else x := 2;
                end
        """
        expect = "Error on line 2 col 23: ("
        self.assertTrue(TestParser.test(input,expect,244))

    def test_45(self):
        input = """
        Function checkArithmeticProgression(A:Mang20;  N:Integer; k:Integer):Boolean;
                Var flag :boolean;
                i :Integer;
                Begin
                    for i:=1 to N do
                    if(A[i] <> A[i-1] + k) then
                    flag:=false;     // Cham dut, ket qua: khong phai
                    return flag; {Ket qua kiem tra la mang cap so cong}
                End
        """
        expect = "Error on line 2 col 46: Mang20"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_46(self):
        input = """
        Function checkArithmeticProgression(A:Mang20;  N:Integer; k:Integer):Boolean;
                Var flag :boolean;
                i :Integer;
                Begin
                    for i:=1 to N do
                    if(A[i] <> A[i-1] + k) then
                    flag:=false;     // Cham dut, ket qua: khong phai
                    return flag; {Ket qua kiem tra la mang cap so cong}
                End
        """
        expect = "Error on line 2 col 46: Mang20"
        self.assertTrue(TestParser.test(input,expect,246))

    def test_47(self):
        input = """
        procedure main();
        begin
            a:= 5;

            if( a < 20 ) then
                writeln("a is less than 20 " );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_48(self):
        input = """
        procedure main();
        begin
            a:= 5;

            if( a < 20 ) then
                writeln("a is less than 20 " );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_49(self):
        """More complex program"""
        input = """
        Function checkSymmetric (A:array[0 .. 10] of REAL; N:Integer ) : Boolean;
                Var Flag:Boolean;
                    i :Integer;
                Begin
                Flag:=True;
                For  i :=1 to N do
                If(A[i] <> A[N-i  +1]) Then
                Flag :=False;       { Cham dut kiem tra, ket qua qua trinh : khong doi xung }
                return flag;
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_50(self):
        input = """
        function max(num1, num2: integer): integer;

        var
        (* local variable declaration *)
        result: integer;
        
        begin
        if (num1 > num2) then
            result := num1;
        
        else
            result := num2;
            max := result;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_51(self):
        input = """var a: array[2 .. 10] of real;
            b,c: integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))

    
    def test_52(self):
        input = """
                var
            a, b, ret : integer;
        (*function definition *)
        function max(num1, num2: integer): integer;
        var
           (* local variable declaration *)
            result: integer;
        begin
            if (num1 > num2) then
            result := num1;
            else
            result := num2;
            max := result;
        end
        begin
        end
        """
        expect = "Error on line 16 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_53(self):
        input = """
                var
        a, b, c,  min: integer;
        procedure findMin(x, y, z: integer; m: integer); 
        (* Finds the minimum of the 3 values *)
        
        begin
            check: boolean;
            if x < y then
            m:= x;
            else
            m:= y;
        
            if z < m then
            m:= z;
        end { end of procedure findMin }  
        
        procedure main();
        begin
            writeln(" Enter three numbers: ");
            readln( a, b, c);
            findMin(a, b, c, min); (* Procedure call *)
        
            writeln(" Minimum: ", min);
        end
        """
        expect = "Error on line 8 col 17: :"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_54(self):
        input = """
                var
            a, b : integer;
        (*procedure definition *)
        procedure swap(x, y: integer); 

        var
            temp: integer;

        begin
            temp := x;
            x:= y;
            y := temp;
        end

        procedure main();
        begin
            a := 100;
            b := 200;
            writeln("Before swap, value of a : ", a );
            writeln("Before swap, value of b : ", b );

            (* calling the procedure swap  by value   *)
            swap(a, b);
            writeln("After swap, value of a : ", a );
            writeln("After swap, value of b : ", b );
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))


    def test_55(self):
        input = """
        A:array[0 .. 10] of REAL
        """
        expect = "Error on line 2 col 8: A"
        self.assertTrue(TestParser.test(input,expect,255))
    
    def test_56(self):
        input = """
        fun()[69]:array[0 .. 10] of REAL
        """
        expect = "Error on line 2 col 8: fun"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_57(self):
        input = """
        VAR Hours, Pay: INTEGER;
        PROCEDURE main();
        """
        expect = "Error on line 4 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_58(self):
        input = """
        var
            greetings: string;
            name: array [1 .. 10] of integer;
            organisation: string;

        procedure main();
        begin
            greetings := "Hello ";
            message := "Good Day!";

            writeln("Please Enter your Name");
            readln(name);
        with
            writeln("Please Enter the name of your Organisation");
            readln(organisation);

            writeln(greetings, name, " from ", organisation);
            writeln(message); 
        end
        """
        expect = "Error on line 15 col 19: ("
        self.assertTrue(TestParser.test(input,expect,258))

    def test_59(self):
        input = """
        var
        a, b, c: integer;
        procedure display();
        var
        """
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,259))

    def test_60(self):
        input = """
                var
        a, b, c: integer;
        procedure display();
        var
        x, y, z: integer;
        """
        expect = "Error on line 7 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_61(self):
        input = """
        procedure swap(x, y: integer); 
        var
            temp: integer;
        beGin
        var A:array[0-100 .. a-10] of REAL;
        begin
            temp := x;
            x:= y;
            y := temp;
        end
        end
        """
        expect = "Error on line 6 col 8: var"
        self.assertTrue(TestParser.test(input,expect,261))

    def test_62(self):
        input = """
        Procedure Array1D(A : array[0 .. 10] of integer;N:Integer);
                Var i: Integer;
                Begin
                Write("N=");
                Readln( N);
                For i:=0 to N do
                    Begin
                        Write("N[", i,"]= ");
                        Readln( A[i] );
                    End
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))

    def test_63(self):
        input = """
        function statement(c: real): integer;
        BEGIN
            if()
            then
            statement(3,a+1,a<>1,a[1]);
            return 1;
            else
            return;
        END
        """
        expect = "Error on line 4 col 15: )"
        self.assertTrue(TestParser.test(input,expect,263))

    
    def test_64(self):
        input = """
        Procedure Array1D(A : array[0 .. 10] of integer;N:Integer);
        begin
        Procedure Sum(a, c:Real);
        begin
        end
        end
        """
        expect = "Error on line 4 col 8: Procedure"
        self.assertTrue(TestParser.test(input,expect,264))

    
    def test_65(self):
        input = """
        Var
            S : String;
            i : Real;

        Procedure main();
        Begin
            i := -0.563;
            Str(i, S);
            Write(S);
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    
    def test_66(self):
        input = """
        Function GetSize() : Integer;
        Begin
        GetSize := topPointer;
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
    
    def test_67(self):
        input = """
        
        Var Ch : String;

        Procedure main();
        Begin
        Writeln("Press \\"\\"q\\"\\" to exit...");
        Ch := Readkey();
        While Ch <> "q" do
        Begin
            Writeln("Please press \\"\\"q\\"\\" to exit.");
            Ch := Readkey();
        End
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
    
    def test_68(self):
        input = """
        procedure main();
        begin
            writeln("Please enter your first name: ");
            readln(firstname);

            writeln("Please enter your surname: ");
            readln(surname);
            /""''""
            writeln();
            writeln(message, " ", firstname, " ", surname);
        end
        """
        expect = "Error on line 9 col 12: /"
        self.assertTrue(TestParser.test(input,expect,268))

    def test_69(self):
        input = """
        EOF
        """
        expect = "Error on line 2 col 8: EOF"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_70(self):
        input = """
        procedure main();
        begin
            a:= 10;
            (* check the boolean condition using if statement *)

            if( a < 20 ) then
            (* if condition is true then print the following *)
            writeln("a is less than 20 " );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
    
    def test_71(self):
        input = """
        VAR Pennies:  INTEGER;
        Tendered, Cost,  Remainder: REAL;
        PROCEDURE Main();
        BEGIN
        (* Input  necessary information *)
        Write("Enter cost  of item: ");
        Read(Cost);
        Write("Enter  amount tendered: ");
        Read(Tendered);
        (* Compute the  change in pennies *)
        Remainder :=  Tendered - Cost;
        Pennies := 0;
        WHILE Remainder  > 0 DO BEGIN
        Remainder :=  Remainder - 0.01;
        Pennies :=  Pennies + 1;
        END (* WHILE *)
        (* Output all  required Results *)
        Write("Cost is:  ");
        Write(Cost);
        Write(" Amount  tendered is: ");
        Write(Tendered);
        Write(" Change  is: ");
        WriteLn(Pennies);
        END (*  BadChanger *)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))

    def test_72(self):
        input = """
        var i: integer ;
                function f(): integer ;
                begin
                    return 200;
                end
                procedure main() ;
                var
                    main: integer ;
                begin
                    main := f() ;
                    putIntLn(main);
                    with
                        i: integer;
                        main: integer;
                        f: integer;
                    do begin
                        main := f := i:= 100;
                        putIntLn (i);
                        putIntLn (main );
                        putIntLn (f);
                    end
                    putIntLn (main);
                end
                var g: real ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def test_73(self):
        input = """
        procedure main();
        begin
            writeln("27e1615212f3c6ea846ed6c412df1361ce97f006ee20bb5aa2483a3b61d5cadd");
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_74(self):
        input = """
        var
        a: integer;

        procedure main();
        begin
            for a := 10  to 20 do
                b: integer;
            begin
                writeln("value of a: ", a);
            end
        end
        """
        expect = "Error on line 8 col 17: :"
        self.assertTrue(TestParser.test(input,expect,274))

    def test_75(self):
        input = """
        var
            a: integer;

        procedure main();
        begin
            a := := 10;
            while  a < 20  do

            begin
                writeln("value of a: ", a);
                a := a + 1;
            end
        end
        """
        expect = "Error on line 7 col 17: :="
        self.assertTrue(TestParser.test(input,expect,275))

    def test_76(self):
        input = """
        pROCEDURE foo(c: real) ;
            BEGIN
                with a , b : integer ; c : array [1 .. 2] of real;
            END
        """
        expect = "Error on line 5 col 12: END"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_77(self):
        input = """
        pROCEDURE foo(c: real) ;
            BEGIN
            with a , b : integer ; c : array [1 .. 2] of real ;
            d := c [a] + b ;
            END
        """
        expect = "Error on line 5 col 14: :="
        self.assertTrue(TestParser.test(input,expect,277))

    def test_78(self):
        input = """
        var x:real ;
            BEGIN
                whILe(a<>1) do beGin
                    if(a=1) then;
                    foo();
                end
            END
        """
        expect = "Error on line 3 col 12: BEGIN"
        self.assertTrue(TestParser.test(input,expect,278))


    def test_79(self):
        input = """
        FUNcTION foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                var x,y: real ;
                END
                BEGIN
        """
        expect = "Error on line 4 col 16: END"
        self.assertTrue(TestParser.test(input,expect,279))


    def test_80(self):
        input = """
        proceDure Hello(a, b:integer);
                begin
                    a := b + c;
                    writeln("Hello, world!");
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))

    def test_81(self):
        input = """
        var
        a: integer;

        procedure main();
begin
    a := 10;
   (* while loop execution *)
    while  a < 20 do

    begin
        writeln("value of a: ", a);
        a:=a +1;

        if( a > 15) then
         (* terminate the loop using break statement *)
    break;
    end
        """
        expect = "Error on line 19 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,281))

    def test_82(self):
        input = """
        Var 
        S1, S2 : String;

        Procedure main();
        Begin
        S1 := "Hey!";
        S2 := " How are you?";
        Write(S1 + S2); { "Hey! How are you?" }
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_83(self):
        input = """
        Var 
        S1, S2, S3 : String;

        Procedure main();
        Begin
        S1 := "Woaw!";
        S2 := " Viet ";
        S3 := " is such a handsome man!";
        Write(S1 + S2 + S3); { "Woaw! Viet is such a handsome man!" }
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_84(self):
        input = """
        Procedure Main();
        Begin
            While 1 do
            Begin
                myIntArray[i] := 1;
                myBoolArray[i] := True;
            End
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_85(self):
        input = """
        var
            a, b, c: integer;
        procedure display();

        var
            a, b, c: integer;
        """
        expect = "Error on line 8 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_86(self):
        input = """
        writeln("Winthin the procedure display");
        writeln("Winthin the procedure display");
        writeln("Winthin the procedure display");
        """
        expect = "Error on line 2 col 8: writeln"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_87(self):
        input = """
        procedure main();
        begin
            a:= 10;
            (* check the boolean condition using if statement *)

            if( a < 20 ) then
              (* if condition is true then print the following *) 
                writeln("a is less than 20 " );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def test_88(self):
        input = """
        procedure main();
        begin
            a := 10;
            (* while loop execution *)
            while  a < 20 do

            begin
                writeln("value of a: ", a);
                a:=a +1;

                if( a > 15) then
                 (* terminate the loop using break statement *)
                break;
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_89(self):
        input = """
        procedure main();
        begin
            a := 100;
            (* check the boolean condition *)
            if( a < 20 ) then
              (* if condition is true then print the following *)
            writeln("a is less than 20" );

            else
              (* if condition is false then print the following *) 
            writeln("a is not less than 20" );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))

    def test_90(self):
        input = """
        begin
        if (num1 > num2) then
            result := num1;

        else
            result := num2;
        max := result;
        end

        begin
            a := 100;
            b := 200;
           (* calling a function to get max value *)
            ret := max(a, b);

            writeln( "Max value is : ", ret );
        end
        """
        expect = "Error on line 2 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,289))

    def test_90(self):
        input = """
        pROCEDURE foo(c: real) ;
            BEGIN
            with a , b : integer ; c : array [1 .. 2] of real ;
            d := c [a] + b ;
            END
        """
        expect = "Error on line 5 col 14: :="
        self.assertTrue(TestParser.test(input,expect,290))

    def test_91(self):
        input = """
        proceDure Hello(a, b:integer);
                begin
                    writeln("Hello, world!");
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_92(self):
        input = """
        procedure main((()) ;
                beGin
                if a=b then if c = d then e := f;
                else i := 1;
                else x := 2;
                end
        """
        expect = "Error on line 2 col 23: ("
        self.assertTrue(TestParser.test(input,expect,292))

    def test_93(self):
        input = """
        Function checkArithmeticProgression(A:Mang20;  N:Integer; k:Integer):Boolean;
                Var flag :boolean;
                i :Integer;
                Begin
                    for i:=1 to N do
                    if(A[i] <> A[i-1] + k) then
                    flag:=false;     // Cham dut, ket qua: khong phai
                    return flag; {Ket qua kiem tra la mang cap so cong}
                End
        """
        expect = "Error on line 2 col 46: Mang20"
        self.assertTrue(TestParser.test(input,expect,293))
    def test_94(self):
        input = """
        Function checkArithmeticProgression(A:Mang20;  N:Integer; k:Integer):Boolean;
                Var flag :boolean;
                i :Integer;
                Begin
                    for i:=1 to N do
                    if(A[i] <> A[i-1] + k) then
                    flag:=false;     // Cham dut, ket qua: khong phai
                    return flag; {Ket qua kiem tra la mang cap so cong}
                End
        """
        expect = "Error on line 2 col 46: Mang20"
        self.assertTrue(TestParser.test(input,expect,294))
    def test_95(self):
        input = """
        procedure main();
        begin
            a:= 5;

            if( a < 20 ) then
                writeln("a is less than 20 " );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))
    def test_96(self):
        input = """
        writeln("Winthin the procedure display");
        writeln("Winthin the procedure display");
        writeln("Winthin the procedure display");
        """
        expect = "Error on line 2 col 8: writeln"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_97(self):
        input = """
        procedure main();
        begin
            a:= 10;
            (* check the boolean condition using if statement *)

            if( a < 20 ) then
              (* if condition is true then print the following *) 
                writeln("a is less than 20 " );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))

    def test_98(self):
        input = """
        procedure main();
        begin
            a := 10;
            (* while loop execution *)
            while  a < 20 do

            begin
                writeln("value of a: ", a);
                a:=a +1;

                if( a > 15) then
                 (* terminate the loop using break statement *)
                break;
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))

    def test_99(self):
        input = """
        procedure main();
        begin
            a := 100;
            (* check the boolean condition *)
            if( a < 20 ) then
              (* if condition is true then print the following *)
            writeln("a is less than 20" );

            else
              (* if condition is false then print the following *) 
            writeln("a is not less than 20" );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))

    def test_100(self):
        input = """
        begin
        if (num1 > num2) then
            result := num1;

        else
            result := num2;
        max := result;
        end

        begin
            a := 100;
            b := 200;
           (* calling a function to get max value *)
            ret := max(a, b);

            writeln( "Max value is : ", ret );
        end
        """
        expect = "Error on line 2 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,300))