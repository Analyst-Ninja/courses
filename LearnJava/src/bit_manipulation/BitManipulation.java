package bit_manipulation;

public class BitManipulation {
    public static void main(String[] args) {
        // Get Bit
        // Step 1. Bit Mask: 1 << pos;
        // Step 2. AND: bitMask & number
        // Step 3. Compare:
        //                  if 0 -> bit was zero
        //                  if 1 -> bit was one
        int n = 5;
        int pos = 1;
        // Creating bitMask
        int bitMask = 1<<pos;

        if ((bitMask & n) == 0){
            System.out.println("bit was zero");
        } else {
            System.out.println("bit was one");
        }

        // Set Bit
        // Step 1. Bit Mask: 1 << pos;
        // Step 2. OR: bitMask | number
        // Step 3: Assign to newNumber

        int newNumber = bitMask | n;
        System.out.println("New number: " + newNumber);

        // Clear Bit: Means making the bit at index to 0
        // Step 1. Bit Mask: 1 << pos;
        // Step 2. AND with NOT

        int bitMaskNOT = ~bitMask;
        int newNumber2 = bitMaskNOT & n;
        System.out.println("New number: " + newNumber2);

        // Update Bit
        // Case 1:
            // For making 0 (0) --> It is just like clearing bit;
            // Bit Mask: 1<<pos;
            // Operation: AND with NOT

            // For making 1 (1) --> It is just like setting bit;
            // Bit Mask: 1<<pos;
            // Operation: OR

        int oper = 1; // if 1 then update bit else clear bit
        if (oper == 1){
            int bitMaskForUpdate = 1<<pos;
            int newNumber3 = bitMaskForUpdate | n;

            System.out.println("New number: " + newNumber3);
        } else {
            int bitMaskForUpdate = 1<<pos;
            int bitMaskForUpdateNOT = ~bitMaskForUpdate;
            int newNumber3 = bitMaskForUpdateNOT & n;

            System.out.println("New number: " + newNumber3);
        }



    }
}