-- test
import Data.Maybe
-- ONE
import Data.List
import Char
euler_one = sum ( filter ( isMultiple ) [1..999] ) where isMultiple x = mod x 5 == 0 || mod x 3 == 0

-- TWO

fibList xs n n1 = if ( n + n1 ) > 4000000 then xs else fibList (xs ++ [n+n1]) (n1) (n+n1)
euler_two = sum ( filter ( even ) ( fibList [] 0 1 ) )

isComposite x = any ( isDivisibleBy x ) [2..floor (sqrt ( fromIntegral x ) )]
isPrime x = not ( isComposite x )

factorList x = concat ( catMaybes (map ( checkFactors x ) possibles ) )
                where checkFactors x1 n1 | isDivisibleBy x1 n1 == False = Nothing
                      checkFactors x1 n1 = Just [n1, x1 `div` n1]
                      possibles = [2..floor (sqrt ( fromIntegral x ) )]
euler_three = maximum ( filter isPrime ( factorList 600851475143 ) )

-- Four
isPalindrome [x] = True
isPalindrome [x,y] = x == y
isPalindrome xs = ( head xs == last xs ) && isPalindrome ( init ( tail xs ) )
products = map (mapper z) [1..999] where z = [1..999]
mapper x = (\x -> map (*x) y  ) where y = [1..999]
converter :: String -> Integer
converter s = read s
--euler_three = maximum ( map (converter) (filter (isPalindrome ) (map show ( concat products ) )) 
--euler_three = maximum ( map converter ( filter isPalindrome (map show ( concat products ) )  ) )


--Five
isDivisibleBy x n = x `mod` n == 0
euler_five = find ( isDivisibleByAll ) [232792550..232792570]
                where isDivisibleByAll x = all ( isDivisibleBy x ) [1..20]

--find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum
euler_six = sum ( map ( **2 ) [1..100] ) - (( sum [1..100] ) **2 )

--isComposite :: Integer -> Bool
--isComposite 1 = True
--isComposite x = any ( isDivisibleBy x ) [ 2 .. floor(sqrt(fromIntegral x)) ]
                --where isDivisibleBy x n = x `mod` n == 0
--isPrime x = not ( isComposite x )

euler_seven = last ( take 10001 ( primeNums ) )
                    where primeNums = filter isPrime [1..] 

euler_eight_data = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

nextFiveDigits xs | length xs < 5 = []
nextFiveDigits xs = [( take 5 xs )] ++ (nextFiveDigits ( tail xs ) )
euler_eight = maximum( map ( mult ) ( map ( map (digitToInt) ) ( nextFiveDigits euler_eight_data ) ))
                    where mult = foldl (*) 1
                
euler_ten = sum ( allPrimes )
                where allPrimes = filter ( isPrime ) [1..2000000]

primes = sieve [2..]
sieve ( p : xs ) = p : sieve [ x | x <- xs, x `mod` p > 0 ]


euler_whatever =  sum $ map digitToInt $ show $ product [1..100]

fib n | n==1 || n ==2 = 1
fib n = fib (n-2) + fib (n-1)
euler_25' n n1 i = if numDigitsInAnswer > 999 then (i, newFib)
                    else euler_25' newFib n (i+1)
                        where numDigitsInAnswer = length $ show newFib
                              newFib = n+n1

euler_shit = reverse $ take 10 $ reverse $ show $ sum ( map (\x -> x^x) [1..1000] )
        
