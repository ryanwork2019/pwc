# pwc
This code is used to visualize the "Practical Worst Case" concept in Lean Manufacturing.

Any process consists of multiple steps. There's always one step in the process that takes the longest time to complete the job, and it determines the overall throughput rate. In Lean Manufacturing, this term is defined as "constraint" or "bottleneck".

If there's no waiting time in the process (the ideal case), the maximum number of units we can produce is throughput rate*(step 1 processing time + step 2 processing time + ... + step n processing time). The result is called "critical WIP". If the company makes products beyond critical WIP, the throughput rate won't increase anymore, and this will only cause a longer lead time.

However, if the number of product units is below the critical WIP, the bottleneck will starve and have idle time, which should be avoided.

In the book "Factory Physics", the author mentioned a concept called "practical worst case" to predict the largest variation a manufacturing plant should have. The two curves represent the exemplary case and the worst case respectively. Any processes that fall between the ideal line and the PWC line are indicated as "Lean". A process that falls below the PWC line is "non-Lean", and there's no process that can be beyond the best-case because that's not feasible.
