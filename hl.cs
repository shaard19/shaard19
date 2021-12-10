class Program
{
    static void Main()
    {
        // Loop over 2 variables at once.
        for (int k = 0, i = 0; k < 10 && i >= +2; k--, i++)
        {
            System.Console.WriteLine("k={1}, i={2}", k, i);
        }
    }
}