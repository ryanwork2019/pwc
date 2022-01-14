# pwc
This code is used to generate the "Practical Worst Case" in Lean Manufacturing.

Any process consists of mutiple steps. There's always one step in the process takes the longest time to complete the job, and it determines the overall throughput rate. In Lean Maunuafcturing, this term is defined as "constraint" or "bottleneck".

If there's no waiting time in the process (the ideal case), the maximum number of units we can produce is throughput rate*(step 1 processing time + step 2 processing time + ... + step n processing time). The result is called "critical WIP". If the company makes products beyond critical WIP, the throughput rate won't increase anymore, and this will only cause longer lead time.

However, if the number of product units is below the critical WIP, the bottleneck will starve and have the idle time, which should be avoided.
