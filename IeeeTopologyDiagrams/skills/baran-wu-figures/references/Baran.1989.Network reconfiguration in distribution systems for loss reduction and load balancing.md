

1989.Network_reconfiguration_in_distribution_systems_for_loss_reduction_and_load_balancing.pdf
IEEE Transactions on Power Delivery, Vol. 4, No. 2, April 1989

# NETWORK RECONFIGURATION IN DISTRIBUTION SYSTEMS FOR LOSS REDUCTION AND LOAD BALANCING

Mesut E. Baran

Felix F. Wu

Department of Electrical Engineering and Computer Sciences

University of California, Berkeley

Berkeley, CA 94720

Abstract - Network reconfiguration in distribution systems is realized by changing the status of sectioning switches, and is usually done for loss reduction or for load balancing in the system. In this paper, general formulation and solution methods are proposed for these problems. In network reconfiguration for loss reduction, the solution involves a search over relevant radial configurations. To aid the search, two approximate power flow methods with varying degree of accuracy have been developed. The methods are computationally attractive and in general give conservative estimates of loss reduction. For load balancing, a load balance index is defined and it is shown that the proposed solution method for loss reduction can also be used for load balancing. Test results are included to show the performance of the proposed method.

Keywords: distribution automation, distribution system operation, distribution system planning, power flow analysis, combinatorial optimization.

## [I. INTRODUCTION](#目录)

In primary distribution systems, sectionalizing switches are used for both protection, to isolate a fault, and for configuration management, to reconfigure the network. Fig.1 shows a schematic diagram of a simplified primary circuit of a distribution system together with sectionalizing switches.

![!\[Figure 1\](python/v2/Figure 1 - Schematic diagram of a primary circuit of a distribution system.png)](<python/v2/Figure 1 - Schematic diagram of a primary circuit of a distribution system.png>)

**Figure 1: Schematic diagram of a primary circuit of a distribution system**

In the figure, load points, where the distribution transformers are tapped off from the primary circuit, is marked by dots, " · " As also shown in the figure, there are two types of switches in the system: normally closed switches connecting the line sections (CB1 - CB6), and normally open switches on the ti-lines connecting either two primary feeders (CB7), or two substations (CB8), or loop-type laterals (CB9).

Distribution systems are normally operated as radial networks; however, configuration is changed during operation by changing the state of some sectionalizing switches. For example, in Fig.1, switches CB7 and CB8 can be closed and CB3 and CB6 can be opened to transfer load from one feeder to another.

Especially with the introduction of remote control capability to the switches, on-line configuration management become an impoertant part of distribution automation. An important operation problem in configuration management is network reconfiguration. As the operating conditions change, the network is reconfigured for two purposes: (i) to reduce the system power loss, (ii) to relieve the overloads in the network. We will refer to the first problem as network reconfiguration for loss reduction and second as load balancing. Another configuration management operation involves the restoration of service to as many costumes as possible during a restorative state following a fault. This problem is called service restoration and can be treated as a special load balancing problem. The network reconfiguration for loss reduction can also be used in planning studies with a different interpretation; namely, to decide through which feeders the new customers are to be supplied.

The early studies on the network reconfiguration were directed to the planning stage \[3-5]. In planning, the main objective is to minimize the cost of construction. An early work on network reconfiguration for loss reduction is presented by A. Merlyn \[6]. His solution scheme starts with a meshed distribution system obtained by considering all switches closed and then the switches are opened successively to eliminate the loops. An equivalent linear resistive network model is used to determine the branches to be opened. In a study done by Ross et al. \[7], two different search algorithms are given for feeder reconfiguration. They developed some indices to measure the degree of constraint violations and used them to obtain a feasible point when the operation point is not feasible. These indices are also used to check the optimality of the solution for power loss reduction.Recently, Civanlar et al. \[10] presented a computationally attractive solution procedure for power loss reduction through network reconfiguration. A simple formula was derived based on some simplifying assumptions to calculate the loss reduction as a result of a load transfer between two feeders.

In \[7], a detailed recipe for service restoration is given by using the indices developed for feasibility. In \[8], Castro et al. proposed simple search techniques for service restoration and load balancing considering data base and implementation requirements for on-line distribution automation applications. Castro and Franca \[9] recently proposed modified search algorithms for service restoration and for load balancing. A modified Fast Decoupled Load Flow is used to check the operating constraints. Aoki et al. proposed more detailed search methods for service restoration and feeder load balancing in \[11] and \[12] respectively. They consider the capacity and voltage constraints and use an approximate power flow solution algorithm to determine the loads to be transferred between the two feeders/transformers.

In this paper, we consider the network reconfiguration problem for both loss reduction and load balancing. We follow the solution approach proposed by Civanlar et al. However, here we introduce two different methods, with varying degree of accuracy, to approximate power flow in the system after a load transfer between two substations, feeders, or laterals. The methods make use of a new set of power flow equations which have been developed specially for radial distribution feeders and used in the capacitor placement problem \[13]. We use these approximate power flow methods to estimate both loss reduction and load balance in the system. Because reactive power flows are explicitly included in the equations, the methods can also be used for systems that are not well compensated.

The organization of the rest of the paper is as follows. A general formulation of the problem is given in the next section and a general search algorithm is presented in section 3. In section 4 and 5, the estimation methods for loss reduction and load balance are given respectively. The proposed methods have been programmed and tested and the results are given in section 6. Conclusions are given in section 7.

## [II. FORMULATION OF THE PROBLEM](#目录)

In this section, the network reconfiguration problems for both loss reduction and load balancing are formulated and their similarities are pointed out.

### 2.1 Problem Statement

To simplify the presentation, we will represent the system on a phase basis and the loads along a feeder section as constant P,Q loads placed at the end of the lines. We also assume that every switch is associated with a line in the system. For example, we assume that the system of Fig.1 can be translated to an equivalent network shown in Fig.2.

![alt text](image-1.png)
**Figure 2: One line diagram of a small distribution system**

In the figure, solid branches represent the lines that are in service and constitute the base radial configuration. Dotted branches (branches 20,21,22) represent the lines with open switches.


The base network can be reconfigured by first closing an open branch, say branch 21 in the figure. Since this switching will create a loop in the system (composed of branches 1, 2, 3, 21, 11, 10, 9, 8, 7, and 15), a branch in the loop containing a switch has to be opened, say branch 7, to restore the radial structure of the system. As a result of this switching, the loads between the branches 7-11 will be transferred from one feeder to the other. We will use the same terminology used in \[7] and call this basic switching operation a branch exchange between branches 21 and 7. In general, as illustrated in the introduction, more complex switching schemes are possible; we will simulate such cases by applying several branch exchanges successively.

The load transfer between different substations can be simulated by branch-exchange type switchings too. In this case, substation nodes (node SS1 and SS2 in the figure) will be considered as a common node although they are not the same node. The methods to be presented in this paper can handle both cases. This is an important property of the proposed methods.

The network reconfiguration problems for loss reduction and load balancing involve the same type of operation, namely the load transfer between the feeders or substations by changing the positions of switches. They only differ in their objective. Other factors, such as the voltage profile of the system, capacities of the lines/transformers, reliability constraints can be considered as constraints.

To state these problems as optimization problems, note that the radial configuration corresponds to a "spanning tree" of a graph representing the network topology. Thus, we have a so-called minimal spanning tree problem which can be stated as follows. Given a graph, find a spanning tree such that the objective function is minimized while the following constraints are satisfied: (i) voltage constraints, (ii) capacity constrains of lines/transformers, (iii) reliability constraints.

This is a combinatorial optimization problem since the solution involves the consideration of all possible spanning trees.

### 2.2 Power Flow Equations

To calculate the terms in optimization problem defined in the previous section, we will use a set of power flow equations that are structurally rich and conducive to computationally efficient solution schemes \[13]. To illustrate them, consider the radial network in Fig.3.

![alt text](image-2.png)
**Figure 3: One line diagram of a radial network**

We represent the lines with impedances $z_l = r_l + jx_l$, and loads as constant power sinks, $S_L = P_L + jQ_L$.

Power flow in a radial distribution network can be described by a set of recursive equations, called DistFlow branch equations, that use the real power, reactive power, and voltage magnitude at the sending end of a branch - $P_i, Q_i, V_i$ respectively to express the same quantities at the receiving end of the branch as follows.

$$
\begin{align*}
P_{i+1} &= P_i - r_i \frac{P_i^2 + Q_i^2}{V_i^2} - P_{Li+1} 
\end{align*}\quad (1.i)
$$

$$
\begin{align*}
Q_{i+1} &= Q_i - x_i \frac{P_i^2 + Q_i^2}{V_i^2} - Q_{Li+1} 
\end{align*}\quad (1.ii)
$$"

$$
\begin{align*}
V_{i+1}^2 &= V_i^2 - 2(r_i P_i + x_i Q_i) \\
&\phantom{=} + (r_i^2 + x_i^2) \frac{P_i^2 + Q_i^2}{V_i^2} 
\end{align*}\quad (1.iii)
$$

Hence, if $P_0, Q_0, V_0$ at the first node of the network is known or estimated, then the same quantities at the other nodes can be calculated by applying the above branch equations successively. We shall refer to this procedure as a forward update.

DistFlow branch equations can be written backward too, i.e., by using the real power, reactive power, and the voltage magnitude at the receiving end of a branch, $P_i, Q_i, V_i$ to express the same quantities at the sending end of the branch. The result is the following recursive equations, called the backward branch equations,

$$
\begin{align*}
P_{i-1} &= P_i + r_i \frac{P_i'^2 + Q_i'^2}{V_i^2} + P_{Li} 
\end{align*}\qquad (2.i)
$$"

$$
\begin{align*}
Q_{i-1} &= Q_i + x_i \frac{P_i'^2 + Q_i'^2}{V_i^2} + Q_{Li} 
\end{align*}\qquad (2.ii)
$$

$$
\begin{align*}
V_{i-1}^2 &= V_i^2 + 2(r_i P_i' + x_i Q_i') \\
&\phantom{=} + (r_i^2 + x_i^2) \frac{P_i'^2 + Q_i'^2}{V_i^2} 
\end{align*}\quad (2.iii)
$$

where, $P_i' = P_i + P_{Li}$, $Q_i' = Q_i + Q_{Li}$.

Similar to forward update, a backward update can be defined: start updating from the last node of the network assuming the variables $P_n, Q_n, V_n$ at that point are given and proceed backwards calculating the same quantities at the other nodes by applying Eq.(2) successively. Updating process ends at the first node (node 0) and will provide the new estimate of the power injections into the network, $P_0, Q_0$.

Note that by applying backward and forward update schemes successively one can get a power flow solution as explained in \[13].

### 2.3 Calculation of the Objective Terms

Having a network model, now we can express the power loss and measure the load balance in the system in terms of system variables.

For loss reduction, the objective is to minimize the total $i^2r$ losses in the system, which can be calculated as follows.

$$
\begin{align*}
LP &= \sum_{i=0}^{n-1} r_i \frac{P_i^2 + Q_i^2}{V_i^2} \quad p.u. 
\end{align*}\quad (3)
$$

This will be the objective function, $c_p$ of network reconfiguration for loss reduction.

For load balancing, we will use the ratio of complex power at the sending end of a branch, $S_i$ over its kVA capacity, $S_i^{\max}$ as a measure of how much that branch is loaded. The branch can be a transformer, a tie-line with a sectionalizing switch or simply a line section. Then we define the load balance index for the whole system as the sum of these measures, i.e.,

$$
\begin{align*}
c_b &= \sum \left( \frac{S_i}{S_i^{\max}} \right)^2 \\
&\phantom{=} = \sum \frac{P_i^2 + Q_i^2}{S_i^{\max 2}} 
\end{align*}\quad (4)
$$

This will be the objective function, $c_b$ of load balancing.

As noted before, the two problems are similar. They both require the same data (system parameters and load) and load flow calculation to evaluate the objectives for a given network topology.


## [III. A SEARCH METHOD USING BRANCH EXCHANGES](#目录)

The radial distribution network reconfiguration problems are formulated as combinatorial, nonlinear optimization problems in the previous section. The solution involves the selection, among all possible trees, of the best feasible one (i.e., the one that has an operating point satisfying the constraints and minimizing the objective). Of course, a search examining all possible spanning trees will give the solution, but it would be computationally formidable; since, for one thing, the number of possible spanning trees that can be generated by branch exchanges will be exhaustive for practical size problems, and another, examining a spanning tree requires a power flow solution of the corresponding system to determine the associated objective. Therefore, an efficient search scheme needs to be developed. In this section, we introduce a simple, heuristic solution method to search over relevant spanning trees systematically by using branch exchanges.

As exemplified in the previous section, branch exchanges can be used to create relevant spanning trees starting from a base spanning tree. In general, given a spanning tree $T_0$, we associate a loop with every open branch in the network by considering as if the branch were closed. Fig.4 shows such a loop associated with open branch $b$. Branch exchange creates a new tree by closing an open branch, (branch b in the figure) and by opening a closed branch in the loop (say branch m in the figure).

![alt text](image-3.png)
Figure 4: The loop associated with open branch $b$

The basic idea of the search scheme using branch exchanges is to start with a (feasible) tree and then create new ones successively by implementing one branch-exchange at a time. At each level, the branch-exchange to be implemented is chosen to be the "best one" (the one that improves the objective function the most without any constraint violations) among all the possible trees (children) that can be generated from the current incumbent spanning tree (parent) by branch exchanges. The method can be described as an algorithm with the following steps.

Step 1: Given a feasible tree $T_0$ (parent),
    run a Power Flow to determine the operating point.

Step 2: Examine all the children of the parent as follows.
    For each open branch $b$
        - find a new candidate tree, $T$ by
            - identifying the loop
            - deciding on the branch, $m$ to be removed.
        - for the candidate tree, $T$
            - calculate the reduction in objective, $\Delta c_{bm}$.

Step 3: Sort the children (trees examined) by using $\Delta c_{bm}$'s.

Step 4: Find the tree $T^*$ which has the greatest $\Delta c_{bm} > 0$
    and satisfies the feasibility constraints.

Step 5: If there is such a $T^*$,
    then choose $T^*$ as $T_0$ and go to step 1; else stop.

We note the following comments about the search.

● This search does not examine all the possible trees and hence the solu-tion will be locally optimal.

● This search does not examine all the possible trees and hence the solu-tion will be locally optimal.

● Computational efficiency of this algorithm hinges on two things; the selection of branch $m$ to be opened, since it eventually effects the number of searches to be performed, and the calculation of objective terms, $\Delta\zeta$'s, for each calculation requires a new power flow solution. Although the power flow solution can be obtained by DistFlow efficiently, nevertheless, it is desirable to be able to estimate the power flows faster without actually running a DistFlow for each branch exchange considered. This will reduce the DistFlow solutions to one for each search level (iteration).

● The estimated power flows are used in ranking open branches. Therefore, errors in estimated figures may lead to a different search than that of using an exact power flow.

In the next section, two different power flow approximation methods, with varying degree of accuracy, are given for loss reduction. In section 5, it is shown that these methods can also be used for load balancing.

## [IV. APPROXIMATE POWER FLOW METHODS FOR POWER LOSS ESTIMATION](#目录)

In this section, we present two methods to determine the power flow in a radial distribution system approximately. The methods will be used to estimate the power loss reduction due to a branch exchange.

### 4.1 Method 1: Simplified DistFlow Method

#### Estimation of Power Flow

We can simplify the DistFlow branch equations, Eq.(1) by noting that the quadratic terms in the equations represent the losses on the branches and hence they are much smaller than the branch power terms $P_i$ and $Q_i$. Therefore, by dropping these second order terms we can get a new set of branch equations of the following form.

$$
\begin{align*}
P_{i+1} &= P_i - P_{Li+1} 
\end{align*}\qquad (5.i)
$$

$$
\begin{align*}
Q_{i+1} &= Q_i - Q_{Li+1} 
\end{align*}\qquad (5.ii)
$$

$$
\begin{align*}
V_{i+1}^2 &= V_i^2 - 2(r_i P_i + x_i Q_i) 
\end{align*}\qquad (5.iii)
$$

Since the network is radial, the solution for the simplified DistFlow equations can be obtained easily; for a radial network of the type shown in Fig.3, the solution is of the following form.

$$
\begin{align*}
P_{i+1} &= \sum_{k=i+2}^{n} P_{Lk} 
\end{align*}\qquad (6.i)
$$

$$
\begin{align*}
Q_{i+1} &= \sum_{k=i+2}^{n} Q_{Lk} 
\end{align*}\qquad (6.ii)
$$"

$$
\begin{align*}
V_{i+1}^2 &= V_i^2 - 2(r_i P_i + x_i Q_i) 
\end{align*}\qquad (6.iii)
$$

We will call Eq.(6) simplified DistFlow equations and use them in this section for power flow solution of a given network configuration.

The power loss on a branch can now be approximated as

$$
\begin{align*}
LP_i &= r_i \frac{P_i^2 + Q_i^2}{V_i^2} \\
&\phantom{=} \approx r_i (P_i^2 + Q_i^2) \quad p.u. 
\end{align*}\qquad (7)
$$

where, we have used the fact that $V_i^2 \approx 1$ $p.u.$ Then the total system loss is simply the sum of all branch losses, i.e.,

$$
\begin{align*}
L\tilde{P} &= \sum_{i=0}^{n-1} r_i (P_i^2 + Q_i^2) \quad p.u. 
\end{align*}\qquad (8)
$$


#### Estimation of Power Loss Reduction due to a Branch Exchange

Now consider the branch exchange between branches $b$ (originally open) and $m$ (originally closed) in Fig.4. As a result of the simplifying assumptions made above, power flow will change only in the branches constituting the loop shown in the figure. Let the branches in the loop that extends between nodes $o, \dots, k-1$ and $k$ be denoted by the set $L$ and the ones on the other side $(o, \dots, n-1, n$ and $k)$ by the set $R$. Then, as shown in Appendix A, power loss reduction due to this branch exchange can be calculated as

$$
\begin{align*}
\Delta L\tilde{P}_{bm} &= 2P_m(\sum_{l \in L} r_l P_l - \sum_{l \in R} r_l P_l) \\
&\phantom{=} + 2Q_m(\sum_{l \in L} r_l Q_l - \sum_{l \in R} r_l Q_l)\\
&\phantom{=} -(P_m^2+Q_m^2)\left[\sum_{l\in R\cup L}r_l\right] 
\end{align*}\quad (9)
$$

Eq.(9) is a quadratic function of the power transfer $P_m, Q_m, i.e.$,

$$
\begin{align*}
\Delta L\tilde{P}_{bm}(P_m, Q_m) &= 2drp.P_m \\
&\phantom{=} + 2drq.Q_m \\
&\phantom{=} - \text{tr.} (P_m^2 + Q_m^2) 
\end{align*}\quad (10)
$$

where, the coefficients $drp$, $drq$, $tr$ are independent of the branch $m$ considered and can be calculated by using only the original branch flows. $P_l$, $Q_l$. The relationship between the loss reduction $\Delta L\tilde{P}$ and the power transfer $(P,Q)$ is illustrated in Fig.5 assuming $P$ and $Q$ are continuous variables. In the figure, the circle defined by $\Delta L\tilde{P}_b = 0$ divides the $P$-$Q$ plane into two regions such that for any point inside circle $\Delta L\tilde{P}_b(P,Q) > 0$ (positive loss reduction, i.e. losses are reduced), and for any points outside the circle $\Delta L\tilde{P}_b(P,Q) < 0$ (negative loss reduction, i.e. losses are increased).

![alt text](image-4.png)

**Figure 5: Loss reduction as a function of power transfer**

This property of Eq.(10) can be used to avoid checking every branch around the loop for branch exchange. Let us first consider the branch exchange between branches b and k in Fig.4, and call it the nominal branch exchange. The corresponding power transfer will be $P_t, Q_t$ and let this point $(P_t, Q_t)$ be inside the circle on the P,Q plane in Fig.5. Then the points corresponding to the other branch exchanges (like $(P_{k-1}, Q_{k-1})$ in the figure) will be further away from the origin on the P-Q plane than $(P_t, Q_t)$ since $P_{k-1} > P_t$ and $Q_{k-1} > Q_t$. Therefore, we have the following conclusions.

● If $\Delta L\tilde{P}_{bk} < 0$ then

$\Delta L\tilde{P}_{bl} < 0$ $l \in L$ and hence there is no branch in $L$ that can be a candidate for branch exchange.

there is a branch in $L$ that can be a candidate for branch exchange and the branch to be opened should be the one that optimizes $\Delta L\tilde{P}_{bm}$. This can be checked by starting from branch $k$ and searching the branches backward in $L$ until $\Delta L\tilde{P}_{bm}$ is maximum.

We have the following comments about the method.

● This method is efficient computationally. Both the calculation of power loss terms, $\Delta L\vec{P}$ and identification of branches to be exchanged requires only simple calculations.

● Accuracy analysis of the method in Appendix B shows that a weak bound on the error in estimating loss reduction around the loop, $e_p = \Delta L P - \Delta L \tilde{P}$ is

$$
\begin{align*}
-(\frac{1}{V_n^2} - 1)L\tilde{P}_R' + (\frac{1}{V_0^2} - 1)L\tilde{P}_R 
\le e_p \\
\le (\frac{1}{V_k^2} - 1)L\tilde{P}_L - (\frac{1}{V_0^2} - 1)L\tilde{P}_L' 
\end{align*}\quad (11)
$$

where, $L\tilde{P}_R'$ and $L\tilde{P}_L'$ denote the power losses on the branches in $R$ and $L$ respectively after the branch exchange.

● The error bounds in Eq.(11) indicate that the estimate is conservative in the sense that when the loss reduction is large ($\Delta L\tilde{P} \gg 0$), error will tend to be positive, (i.e., $\Delta L\tilde{P} \gg 0 \rightarrow \Delta L\tilde{P} \gg 0$). Similarly when the loss reduction is negative, error will tend to be negative, (i.e., $\Delta L\tilde{P} \ll 0 \rightarrow \Delta L\tilde{P} - \Delta L\tilde{P} \le 0$). However, when the loss reduction figures are small, the error will be two sided. This error analysis shows that there may be some "misses," (i.e., a branch exchange with positive loss reduction may be identified as the one with negative loss reduction) and there may be some "mislabeling," (i.e., a branch exchange with negative loss reduction may be identified as the one with positive loss reduction).

### 4.2 Method 2: Backward and Forward Update of DistFlow Power Flow Update

The second method makes use of the backward and forward updates of DistFlow, introduced in section 2, to update power flow around the loop of a branch exchange. For the nominal branch exchange b-k of Fig.4, the method comprises the following steps.

> Step 1: Backward Update

Update the power flow around the loop by backward update starting from the nodes $k$ and $n$ of the loop and by carrying out the power and voltage updates separately (i.e., use Eq.(2.i) and Eq.(2.ii) with original voltages, $V_i$ to update the powers, and use Eq.(2.iii) to update the voltages). Let the updated powers be

$$
\begin{align*}
&\hat{P}_i', \hat{Q}_i', \quad i=k, \dots, ok; \\
&\hat{P}_i', \hat{Q}_i', \quad i=n, \dots, on 
\end{align*}\quad (12)
$$

and the voltage updates at the common node be $\hat{V}_{on}'$ and $\hat{V}_{ok}'$.

Step 2: Forward Update

Compare the voltage differences at node o (difference between $V_o$ and $\hat{V}_{on}$, $\hat{V}_{ok}$). If the voltage difference is too large (larger than a predefined value, $e^{\max}$), go through a forward update to reduce the error (this time starting from the common node $o$ and using $V_o$, $\hat{P}_{ok}$, $\hat{P}_{on}$ as initial, given values and applying the forward update). Let the updated powers be

$$
\begin{align*}
&\hat{P}_i'', \hat{Q}_i'', \quad i=ok+1, \dots, k; \\
&\hat{P}_i'', \hat{Q}_i'', \quad i=on+1, \dots, n 
\end{align*}\quad (13)
$$


Step 3: Correct the Power Estimate at the Common Node

Use the difference between the updates $\hat{P}_k', \hat{P}_n'$ and $\hat{P}_k'', \hat{P}n''$ as power mismatches and correct $\hat{P}_{on}'$ and $\hat{P}{ok}'$ by adding them the mismatches, i.e.,

$$
\begin{align*}
&\hat{P}_{ok}^{''} = \hat{P}_{ok}^{'} + (\hat{P}_{k}^{'} - \hat{P}_{k}^{''}); \\
&\hat{P}_{on}^{''} = \hat{P}_{on}^{'} + (\hat{P}_{n}^{'} - \hat{P}_{n}^{''}) 
\end{align*}\quad (14)
$$

Details of development of this algorithm is given in Appendix C.

Note that backward and forward update constitutes an iteration of power flow solution using DistFlow branch equations. Here, we exploit the method by localizing it to the loop of branch exchange and performing a special iteration. Therefore:

● the method is computationally more efficient than a full power flow,

● accuracy of the method will mainly depend on load transfer $P_k, Q_k$.

#### Calculation of Power Loss Reduction

For power loss estimation, note that

$$
\begin{align*}
&P_{ok} - \hat{P}_{ok}^{''} = \Delta P_k + \Delta LP_L; \\
&P_{on} - \hat{P}_{on}^{''} = -\Delta P_k + \Delta LP_R 
\end{align*}\quad (15)
$$

where, $\Delta LP_R$ and $\Delta LP_L$ represent the power loss reductions on the $R$ and $L$ sides of the loop respectively. Therefore, the total power loss reduction can be approximated as

$$
\begin{align*}
\Delta L\hat{P} &= \Delta L P_L + \Delta L P_R \\
&= (P_{ok} - \hat{P}_{ok}^{''}) + (P_{on} - \hat{P}_{on}^{''}) \quad (16)
\end{align*}
$$

## [V. LOAD BALANCING WITH BRANCH EXCHANGES](#目录)

When the general search algorithm introduced in section 3 is used for load balancing, the calculations will be similar to that of the loss reduction case. The only difference will be in the calculation of the objective; for load balancing, we need to estimate the value of the new objective, load balance index, $c_b$ for every branch exchange considered during the search.

The objective, given by Eq.(4), can however be calculated by using the two approximate power flow methods introduced in Sec.IV - the simplified DistFlow method and the forward and backward update method, because both of the methods give the approximate power flows in the system following a branch exchange. Once the new power flow in the branches, $P_i$, $Q_i'$ are estimated then the new load balance index can be computed by employing Eq.(4), i.e.,


$$
\begin{align*}
c_b &= \sum \frac{P_i^{''2} + Q_i^{''2}}{S_i^{max2}} 
\end{align*}
$$"

When the two methods are compared for load balancing, simplified DistFlow method seems more attractive because of the following reasons.

● Since the index of load balance is relative, the accuracy of simplified DistFlow method should be adequate.

## [VI. TEST RESULTS](#目录)

The proposed solution method has been implemented in Fortran-77. The approximate power flow methods described in Sec.IV; (M1) - simplified. DistFlow, and (M2) - backward and forward updates of DistFlow, are used to guide the search. In addition, exact power flow method, DistFlow is also used as another method (M3), to check the accuracy of M1 and M2. The test results for loss reduction will be presented here to illustrate the performance of the proposed method.

The test system is a hypothetical 12.66 kV system with a 2 feeder substation, 32 busses, and 5 looping branches (tie lines). The system data is given in Table 1 together with the voltage profile of the base configuration. The total substation loads for the base configuration are 5084.26 kW and 2547.32 kvar. The system is not well-compensated and lossy (the total loss is about 8% of the total load). A lossy system is selected because the loss reduction is expected to be appreciable.

In the test runs, the constraints mentioned in Sec.II are not imposed. In fact, the voltage profile of the base system configuration is lower than the usual lower limit of 0.9 p.u.; which shows that the system is not well configured. Also, it is assumed that every branch in the system is available for branch-exchange.

A summary of the test run is given in Table 2. In the table, each row corresponds to a branch exchange. Branch exchanges are defined by a pair of numbers in second column. The other columns labeled, M1, M2, M3 correspond to searches guided by methods M1, M2, M3 respectively. The row after a search level, row six for example, shows the branch-exchange chosen based on the ordering of the loss reduction figures obtained in that search level.

**Table 2: Test Results**

| search | branch | loss reduction in kW | loss reduction in kW | loss reduction in kW |
| ------ | ------ | -------------------- | -------------------- | ----------------- |
| level  | in-out |   M1   |   M2   |   M3  |
| ---    | ---    |   ---  |  ---   |  ---  |
| 1      | 33-6   |  67.70 |  77.89 | 84.23 |
| 1      | 34-14  |  05.34 |  06.64 | 06.79 |
| 1      | 35-7   |  66.30 |  77.25 | 83.43 |
| 1      | 36-32  |  01.6  |  02.32 | 02.36 |
| 1      | 37-28  |  61.31 |  70.15 | 73.17 |
|        | br-ex  |  33-6  |  33-6  | 33-6  |
| 2      |  6-7   | -01.71 | -02.05 |-02.67 |
| 2      | 34-14  |  05.08 |  05.92 | 06.00 |
| 2      | 35-11  |  16.1  |  17.82 | 18.30 |
| 2      | 36-32  |  02.08 |  03.00 | 03.06 |
| 2      | 37-28  |  08.35 |  05.12 | 05.22 |
|        | br-ex  |  35-11 |  35-11 | 35-11 |
| 3      |  6-7   | -05.19 | -06.42 |-07.07 |
| 3      | 34-14  | -00.65 | -00.80 |-00.82 |
| 3      | 11-10  | -00.16 | -00.19 |-00.22 |
| 3      | 36-31  |  11.76 |  13.63 | 15.77 |
| 3      | 37-28  |  08.35 |  05.12 | 05.22 |
|        | br-ex  |  36-31 |  36-31 | 36-31 |
| 4      |  6-7   | -01.11 | -01.33 |-01.58 |
| 4      | 34-14  | -00.44 | -01.12 |-01.14 |
| 4      | 11-10  | -00.76 | -00.90 |-01.04 |
| 4      | 31-30  | -02.76 | -05.02 |-05.16 |
| 4      | 37-28  |  01.39 | -01.35 |-01.42 |
|        | br-ex  |  37-28 | <br /> |<br /> |
| 5      |  6-33  |  07.20 | <br /> |<br /> |
| 5      | 34-14  | -00.44 | <br /> |<br /> |
| 5      | 11-10  | -00.76 | <br /> |<br /> |
| 5      | 31-32  | -03.0  | <br /> |<br /> |
| 5      | 28-37  |  05.67 | <br /> |<br /> |
|        | br-ex  |   6-33 | <br /> |<br /> |
| 6      | 33-7   | -00.17 | <br /> |<br /> |
| 6      | 34-14  | -08.17 | <br /> |<br /> |
| 6      | 11-10  | -00.74 | <br /> |<br /> |
| 6      | 31-30  | -00.92 | <br /> |<br /> |
| 6      | 28-27  | -03.93 | <br /> |<br /> |

From the test result of Table 2, we have the following observations.

i. In the first search level, the loss reductions are big, they satisfy the conservative property discussed in Sec.III and the errors in estimations are small enough so that the same branch exchange is chosen by all three methods. However, as we go down the search levels, the loss reductions get smaller and the difference between the two estimated values becomes more visible; while estimation figures of M2 consistently satisfy the conservative property and get closer to the exact values, accuracy and conservative property of M1 weakens (estimation becomes two sided). This is particularly true for estimates of branch exchange 37-28.

ii. The three methods lead to the same searches at the upper levels (up to level 4). At level 4, while the searches with M2 and M3 converge to a local optimum as expected, the search with M1, which uses less accurate loss reduction figures, mislabels branch exchange 37-28 (i.e., estimates a negative loss reduction as positive), and performs two more searches leading to the global optimum point. However, the two solutions points have close objective values (total loss reductions at the solution points of M1 and M2, M3 are 125 kW and 118 kW respectively).

iii. Branch exchanges occur on the lower voltage side of the loop.

iv. The voltage profile of the system increases as the loss is minimized. (the minimum bus voltage of the system raises from 0.88 p.u. to 0.92 p.u.).

The last two observations were used as heuristic rules in the search in \[7] and \[10]. However, the observations may not always be true; a counter-example is given in Fig.6, where branch exchange 7-3 is a switching on the higher side and results in a positive loss reduction.

![alt text](image-5.png)
**Figure 6: Example of a branch exchange on the higher voltage side**

From these observations, we have the following suggestions to improve computational and convergence characteristics of the method.

● In general backward and forward update method is more reliable than the simplified DistFlow method in estimating the power loss reduction due to a branch exchange, especially as the loss reduction figures get smaller. Therefore, the decision as to which method to choose should be made by considering the magnitude of loss reduction figures. A scheme compromizing between accuracy and computation would be to start with the simplified DistFlow method and then switch to backward and forward update method as the loss reduction figures get smaller.

● The search scheme gives acceptable solution for practical purposes since even if the solution converges to a local optimal point, the difference between the local solution and the global solution will be small. Furthermore, the convergence characteristics of the search can be improved by checking the locality of the solution. A possible scheme would be to do another quick search implementing more than one branch exchange with big loss reduction at each search level. Then the two solutions can be compared to see if they converge to the same point.

## [VII. CONCLUSIONS](#目录)

In this paper a general formulation of the feeder reconfiguration problem for loss reduction and load balancing is given and a new solution method is presented. The solution employs a search over different radial configurations created by considering branch exchange type switchings.

**Table 1: Network data of the test system**

|$Br.$|$Rc.$|$Sn.$|$Br.Prm.$  |$Br.Prm.$|$Sn.Node.$|$Sn.Node.$|$Sn.Node.$|
| --- | --- | --- | ---       |---      |---       |---       |---       |
|$No$ |$Nd.$|$Nd.$|$r(\Omega)$|$x(\Omega)$|$PL(kW)$|$QL(kvar)$|$V^2$  |
| 1| 0| 1|0.0922|0.0470|100.00| 60.00|0.9927|
| 2| 1| 2|0.4930|0.2511|  90.00| 40.00|0.9574|
| 3| 2| 3|0.3660|0.1864|120.00| 80.00|0.9374|
| 4| 3| 4|0.3811|0.1941| 60.00| 30.00|0.9176|
| 5| 4| 5|0.8190|0.7070| 60.00| 20.00|0.8707|
| 6| 5| 6|0.1872|0.6188|200.00|100.00|0.8641|
| 7| 6| 7|0.7114|0.2351|200.00|100.00|0.8550|
| 8| 7| 8|1.0300|0.7400| 60.00| 20.00|0.8432|
| 9| 8| 9|1.0440|0.7400| 60.00| 20.00|0.8324|
|10| 9|10|0.1966|0.0650| 45.00| 30.00|0.8308|
|11|10|11|0.3744|0.1238| 60.00| 35.00|0.8280|
|12|11|12|1.4680|1.1550| 60.00| 35.00|0.8167|
|13|12|13|0.5416|0.7129|120.00| 80.00|0.8125|
|14|13|14|0.5910|0.5260| 60.00| 10.00|0.8099|
|15|14|15|0.7463|0.5450| 60.00| 20.00|0.8074|
|16|15|16|1.2890|1.7210| 60.00| 20.00|0.8037|
|17|16|17|0.7320|0.5740| 90.00| 40.00|0.8026|
|18| 1|18|0.1640|0.1565| 90.00| 40.00|0.9916|
|19|18|19|1.5042|1.3554| 90.00| 40.00|0.9845|
|20|19|20|0.4095|0.4784| 90.00| 40.00|0.9831|
|21|20|21|0.7089|0.9373| 90.00| 40.00|0.9818|
|22| 2|22|0.4512|0.3083| 90.00| 50.00|0.9504|
|23|22|23|0.8980|0.7091|420.00|200.00|0.9373|
|24|23|24|0.8960|0.7011|420.00|200.00|0.9309|
|25| 5|25|0.2030|0.1034| 60.00| 25.00|0.8643|
|26|25|26|0.2842|0.1447| 60.00| 25.00|0.8557|
|27|26|27|1.0590|0.9337| 60.00| 20.00|0.8201|
|28|27|28|0.8042|0.7006|120.00| 70.00|0.7945|
|29|28|29|0.5075|0.2585|200.00|600.00|0.7816|
|30|29|30|0.9744|0.9630|150.00| 70.00|0.7739|
|31|30|31|0.3105|0.3619|210.00|100.00|0.7723|
|32|31|32|0.3410|0.5302| 60.00| 40.00|0.7717|
|33| 7|20|2.0000|2.0000|   -  |   -  | -    |
|34| 8|14|2.0000|2.0000|   -  |   -  | -    |
|35|11|21|2.0000|2.0000|   -  |   -  | -    |
|36|17|32|0.5000|0.5000|   -  |   -  | -    |
|37|24|28|0.5000|0.5000|   -  |   -  | -    |

To guide the search, two different power flow approximation methods with varying degree of accuracy have been developed and tested. The methods are used to calculate the new power flow in the system after a branch-exchange and they make use of the power flow equations developed for radial distribution systems.

Both accuracy analysis and the test results show that:

● Estimation methods are computationally very efficient and in general give conservative results. They also consider both real and reactive power flows. Therefore, they can be used in searches to reconfigure a given system even if the system is not well compensated and reconfiguring involves load transfer between different subtations.

● The search method introduced in this paper, as well as in \[7], \[10], \[11], has the following appealing properties: it is not exhaustive, it is of order $m^2$ (m is the number of open switches), and it involves about m power flow solutions. Its convergence characteristics is acceptable although it does not guarantee convergence to the global optimum. However, modifications to this basic search is proposed to improve its computational and convergence characteristics whenever it is needed.

For load balancing, a load balance index is defined and it is shown that the search and power flow estimation methods developed for power loss reduction can also be used for load balancing since the two problems are similar. Between the two estimation methods, the second - simplified DistFlow method, seems to be more appropriate for load balancing because of the relative nature of load balancing concept.

## Acknowledgements

This research is supported by TUBITAK-TURKEY and by National Science Foundation under grant ECS-8715132.

## REFERENCES

\[1] Distribution Systems, Westinghouse Electric Corp., East Pittsburgh, PA, 1965.

\[2] "Bibliography on Distribution Automation" IEEE Transactions on Power Apparatus and Systems, vol. PAS 103, June 1984, pp. 1176-1182.

\[3] T. Gonen, A. A. Mahmoud and H. W. Golburn, "Bibliography of Power Distribution System Planning", IEEE Transactions on Power Apparatus and Systems, vol. PAS 102, June 1983, pp. 1178-1787.

\[4] D. I. Sun, D. R. Farris et al., "Optimal Distribution Substation and Primary Feeder Planning via the Fixed Charge Network Formula", IEEE Transactions on Power Apparatus and Systems, vol. PAS 101, March 1982, pp. 602-609.

\[5] E. Lakervi and J. Partenen, "Linear Voltage Regulation and Loss Calculation Methods for Low Voltage Network Design", IEEE Transactions on Power Apparatus and Systems, vol. PAS 103, Aug. 1984, pp. 2249-2253.

\[6] A. Merlin and H. Back, "Search for a Minimal-Loss Operating Spanning Tree Configuration in Urban Power Distribution Systems", Proc. of 5 th Power Systems Comp. Con., Cambridge, U.K., Sept. 1-5, 1975.


\[7] D. W. Ross, M. Carson, A. Cohen, et al., "Development of Advanced Methods for Planning Electric Energy Distribution Systems", DEO final report no SCI-5263, Feb 1980.

\[8] C. H. Castro, J. B. Bunch, and T. M. Topka, "Generalized Algorithms for Distribution Feeder Deployment and Sectionalizing", IEEE Transactions on Power Apparatus and Systems, vol. PAS 99, March/April 1980, pp. 549-557.

\[9] C. A. Castro Jr. and A. L. M. Franca, "Automatic Power Distribution Reconfiguration Algorithm Including Operating Constraints", Proc. of IFAC on Electric Energy Systems, Rio de Janeiro, Brazil, 1985.

\[10] S. Civanlar, J. J. Grainger, and S. H. Lee, "Distribution Feeder Reconfiguration for Loss Reduction", IEEE PES Winter Meeting, Feb. 1987, paper no: 87WM 140-7.


\[11] K. Aoki, H. Kuwabara, T. Satoh, and M. Kanezashi, "An Efficient Algorithm for Load Balancing of Transformers and Feeders by Switch Operation in Large Scale Distribution Systems", IEEE PES Summer Meeting, 1987, paper no: 87SM 543-2

\[12] K. Aoki, T. Satoh, M. Itoh, et al., "Voltage Drop Constrained Restoration of Supply by Switch Operation in Distribution Systems", IEEE PES Summer Meeting, 1987, paper no: 87SM 544-0

\[13] M. E. Baran, and F. F. Wu, "Optimal Sizing of Capacitors Placed on a Radial Distribution System", presented at IEEE PES Winter Meeting , Feb. 1-6, 1988, paper no 88WM 065-5

# APPENDIX

# A. Estimation of Power Loss Reduction due to a Branch Exchange by Simplified DistFlow Method

To calculate the power loss reduction due to a branch exchange, we need to estimate new branch flows after the switching around the loop which is defined by the branch exchange. Note that the branch flows before the switching are known.

To calculate the power loss reduction due to a branch exchange, we need to estimate new branch flows after the switching around the loop which is defined by the branch exchange. Note that the branch flows before the switching are known.

First consider the nominal branch exchange between branch b (originally open) and k (originally closed) of Fig.4. By simplified DistFlow equation of (6), branch flows around the loop, $P_i, Q_i$ will change by $P_k, Q_k$ amount, i.e.,

$$
\begin{align*}
&\left\{
\begin{aligned}
P_i' &= P_i - P_k \\
Q_i' &= Q_i - Q_k
\end{aligned}
\right., \qquad i \in L \qquad (a1.i) \\[4pt]
&\left\{
\begin{aligned}
P_i' &= P_i + P_k \\
Q_i' &= Q_i + Q_k
\end{aligned}
\right., \qquad i \in R \qquad (a1.ii)
\end{align*}
$$

For the general case - branch exchange between branches b and m, it can easily be verified that the branch flows around the loop will change by $P_m, Q_m$, i.e.,

$$
\begin{align*}
&\left\{
\begin{aligned}
P_i' &= P_i - P_m \\
Q_i' &= Q_i - Q_m
\end{aligned}
\right., \qquad i \in L \qquad (a2.i) \\[4pt]
&\left\{
\begin{aligned}
P_i' &= P_i + P_m \\
Q_i' &= Q_i + Q_m
\end{aligned}
\right., \qquad i \in R \qquad (a2.ii)
\end{align*}
$$

Now we can calculate the real power loss reduction due to branch exchange b-m as follows. By Eq.(8), the original total power loss on $L$ and $R$ sides of the loop will be

$$
\begin{align*}
&\left\{
\begin{aligned}
L\tilde{P}_L &= \sum_{l \in L} r_l(P_l^2 + Q_l^2) \\
L\tilde{P}_R &= \sum_{l \notin R} r_l(P_l^2 + Q_l^2)
\end{aligned}
\right. \qquad (a.3)
\end{align*}
$$

These terms can be updated after the branch exchange by using the updated power flows, $P_i', Q_i'$. Let the updated loss terms be $L\tilde{P}_L', L\tilde{P}_R'$. Then the real power loss reduction, $\Delta L\tilde{P}_{bm}$ due to branch exchange b-m will be

$$
\begin{align*}
\Delta L\tilde{P}_{bm} &= \Delta L\tilde{P}_L + \Delta L\tilde{P}_R \\
&= (L\tilde{P}_L - L\tilde{P}_L') + (L\tilde{P}_R - L\tilde{P}_R') \quad (a.4)
\end{align*}
$$

When the loss terms $L\tilde{P}_L$, $L\tilde{P}_R$ are substituted in above equation and the terms are rearranged, power loss reduction can be written only in terms of original branch flows, $P_i$, $Q_i$ as in Eq.(9).

When the loss terms $L\tilde{P}_L$, $L\tilde{P}_R$ are substituted in above equation and the terms are rearranged, power loss reduction can be written only in terms of original branch flows, $P_i$, $Q_i$ as in Eq.(9).

#### B. Accuracy Analysis of Simplified DistFlow Method

We will derive the relation between the actual loss reduction, $\Delta L P$ and the estimated value, $\Delta L P$ due to a branch exchange by simplified DistFlow method in two steps; first power loss reduction along a radial network will be studied, then these results will be used to evaluate the power loss reduction around the loop of a branch exchange.

#### Power Loss Reduction on a Radial Network

Consider the radial network shown in Fig.3. As noted before, such a network represents one side, say side $R$, of the loop of a branch exchange. Let the power change at the end of the network due to branch exchange be $\Delta P_n$, $\Delta Q_n > 0$.

Lets first consider the change in voltage profile as a result of change of power at the end node $n$, $\Delta P_n$, $\Delta Q_n$. A good estimate can be obtained by using the simplified DistFlow equations of (6). From Eq.(6), the change in branch power will be

$$
\begin{align*}
&\left\{
\begin{aligned}
\Delta P_i &= P_i' - P_i = \Delta P_n \\
\Delta Q_i &= Q_i' - Q_i = \Delta Q_n
\end{aligned}
\right., i = 0,...,n 
\end{align*}\quad (b.1)
$$

Assuming $V'_0 = V_o$, change in voltages can be obtained by Eq.(6.iii) as

$$
\begin{align*}
\Delta V_i^2 &= V_i^2 - V_i^2 = -2(\Delta P_n \sum_{k=0}^{i} r_k + \Delta Q_n \sum_{k=0}^{i} x_k) 
\end{align*}\quad (b.2)
$$

Therefore, the voltage profile along the network will drop with an increasing magnitude towards the end of the network, i.e.,

$$
\begin{align*}
\Delta V_n &\le \Delta V_{n-1} \le \dots \le \Delta V_o \approx 0 
\end{align*}\quad (b.3)
$$"

Now consider the new power flow in the network and let the power at the sending end of branch $i$ be as follows.

$$
\begin{align*}
&\left\{
\begin{aligned}
P_i' &= P_i + \Delta P_n + \Delta LP_{i,n} \\
Q_i' &= Q_i + \Delta Q_n + \Delta LQ_{i,n}
\end{aligned}
\right. 
\end{align*}\qquad (b.4)
$$

Then by using the backward equations of (2), it can be shown that

$$
\begin{align*}
&\left\{
\begin{aligned}
P'_{i-1} &= P_{i-1} + \Delta P_n + \Delta LP_{i-1,n} \\
Q'_{i-1} &= Q_{i-1} + \Delta Q_n + \Delta LQ_{i-1,n}
\end{aligned}
\right. 
\end{align*}\qquad (b.5)
$$

1407

$$ \text{where, } \Delta LP_{i-1,n} = \Delta LP_{i,n} \qquad (b.6) $$

The last term in (b.6) is due to the loss reduction on branch $i$, $\Delta LP_i$. Consequently, the terms $-\Delta LP_{i,n}, -\Delta LQ_{i,n}$ represent the actual loss reduction between nodes $i$ and $n$ and have the following property.

$$
\begin{align*}
0 &\le \Delta LP_{n-1,n} \le \dots \le \Delta LP_{o,n} \\
0 &\le \Delta LQ_{n-1,n} \le \dots \le \Delta LQ_{o,n} 
\end{align*}\qquad (b.7)
$$

These terms are of second order, i.e.,

$$
\begin{align*}
&\left\{
\begin{aligned}
|\Delta P_n| &\gg |\Delta LP_{i,n}| \\
|\Delta Q_n| &\gg |\Delta LQ_{i,n}|
\end{aligned}
\right., i = 0,1,\dots,n-1 
\end{align*}\quad (b.8)
$$

Now consider the loss reduction on the network. Power loss reduction on line $l$, $\Delta LP_l$ can be calculated as

$$
\begin{align*}
&\Delta LP_l = LP_l - LP'_l \\
&= r_l\frac{P_l^2+Q_l^2}{V_l^2} \\
&\phantom{=} - r_l\frac{(P_l+\Delta P_n+\Delta LP_{i,n})^2}{V_l^2} \\
&\phantom{=} + r_l\frac{(Q_l+\Delta Q_n+\Delta LQ_{i,n})^2}{V_l^2}
\end{align*}
\qquad (b.9)
$$

The simplified DistFlow method estimates this quantity as

The simplified DistFlow method estimates this quantity as

$$ \begin{align*}
&\Delta LP_l = L\tilde{P}_l - L\tilde{P}_l' \\
&= r_l (P_l^2 + Q_l^2) \\
&\phantom{=} - r_l [(P_l + \Delta P_n)^2 + (Q_l + \Delta Q_n)^2]
\end{align*}
\qquad (b.10) $$

Combining Eq.(b.9) and Eq.(b.10) will give

$$
\begin{align*}
\Delta LP_l &= \frac{1}{V_l^2} L \tilde{P}_l - \frac{1}{V_l^2} L \tilde{P}_l' + \delta LP_l 
\end{align*}\quad (b.11)
$$

$$ \begin{align*}
&\delta LP_l \\
&= \frac{1}{V_l^2} \bigl\{ [r_l (P_l + \Delta P_n)^2 + (Q_l + \Delta Q_n)^2] \\
&\phantom{=} + \frac{1}{V_l^2} r_l [(P_l+\Delta P_n+\Delta LP_{l,n})^2 ]\\
&\phantom{=} - \frac{1}{V_l^2} r_l [(P_l+\Delta P_n+\Delta LP_{l,n})^2 ]\\
&\phantom{=} - \frac{1}{V_l^2} r_l [(Q_l+\Delta Q_n+\Delta LQ_{l,n})^2] \bigr\} \\
&\phantom{=} \le 0
\end{align*}
\qquad (b.12) $$


Eq.(b.12) indicates that $\delta LP_l$ represents the extra loss reduction due to correction terms $\Delta LP_{l,n}$ and $\Delta LQ_{l,n}$ and it is of second order, i.e., $|\delta LP_l| \ll |\Delta LP_l|$. Dropping these second order terms, Eq.(b.11) can be bounded as

$$ \begin{align*}
&\frac{1}{V_l^2} L \tilde{P}_l - \frac{1}{V_l^2} L \tilde{P}_l' \\
&\le \Delta LP_l \\
&\le \frac{1}{V_l^2} \Delta L \tilde{P}_l 
\end{align*}\quad (b.13) $$

Since the total loss on the section is the sum of branch losses, the bound for the whole section will be

$$ \begin{align*}
&\frac{1}{\bar{V}_R^2} L \tilde{P}_R - \frac{1}{\bar{V}_R^2} L \tilde{P}_R' \\
&\le \Delta LP_R \\
&\le \frac{1}{\bar{V}_R^2} \Delta L \tilde{P}_R 
\end{align*}\quad (b.14) $$

where, $\bar{V}_R^2$ and $\bar{V}_R^2$ represent aggregated voltages, i.e.,


$$
\begin{align*}
\frac{1}{\bar{V}_R^2} &= [\sum \frac{1}{V_l^2} L \tilde{P}_l] / \sum L \tilde{P}_l 
\end{align*}\quad (b.15)
$$

Therefore,

$$
\begin{align*}
&\left\{
\begin{aligned}
V_n^2 &\le \bar{V}_R^2 \le V_o^2 \\
V_n^2 &\le \bar{V}_R^2 \le V_o^2
\end{aligned}
\right. 
\end{align*}\qquad (b.16)
$$

By letting

$$
\begin{align*}
&\left\{
\begin{aligned}
\bar{V}_R^2 &\approx V_0^2 \\
\bar{V}_R^2 &\approx V_n^2
\end{aligned}
\right. 
\end{align*}\qquad (b.17)
$$

a weak bound on the error of estimation can be obtained as

$$
\begin{align*}
&(\frac{1}{V_0^2}-1)L\tilde{P}_R - (\frac{1}{V_n^2}-1)L\tilde{P}_R' \\
&\le \Delta LP_R - \Delta L\tilde{P}_R \\
&\le (\frac{1}{V_0^2}-1)\Delta L\tilde{P}_R \le 0 
\end{align*}\qquad (b.18)
$$

#### Power Loss Reduction Around the Loop of a Branch Exchange

Consider the nominal branch exchange of Fig.4. Power loss reduction on the R side of loop is given in the previous section. Now consider the other side, side L, of the branch exchange loop. The same derivation steps of the previous section can be applied for this side also and the bounds on loss reduction error can be obtained by mimicking the derivation of R side. The result will be

$$\begin{align*}
&0 \le (\frac{1}{V_0^2} - 1) \Delta L P_L \\
&\le \Delta LP_L - \Delta L P_L \\
&\le (\frac{1}{V_k^2} - 1) L P_L - (\frac{1}{V_0^2} - 1) L P_L' 
\end{align*}\quad (b.19)$$

Finally, adding Eq.(b.18) and Eq.(b.19), bounds on the total loss reduction error can be written as

$$\begin{align*}
&-(\frac{1}{V_r'^2}-1)L\tilde{P}_R' + (\frac{1}{V_0^2}-1)L\tilde{P}_R \\
&\le \Delta L P - \Delta L P \\
&\le (\frac{1}{V_k^2}-1)L\tilde{P}_L - (\frac{1}{V_0'^2}-1)L\tilde{P}_L'
\end{align*}$$

# C. Development of Method 2

There are three different schemes that can be used to approximate the new power flow in a system after a branch exchange by making use of the backward and forward updates of DistFlow introduced in Sec.II.

Scheme 1: Consider the nominal branch exchange between branches b and k in Fig.4. As shown in Appendix B, the voltage profile around the loop will change in such a way that it will be higher on the L side and lower on the R side than their original values and it satisfies the following relationship.

$$
\begin{align*}
&\Delta V_k^2 = V_k'^2 - V_k^2 \\
&\ge \Delta V_{k-1}^2 \ge \dots \ge \Delta V_o^2 \approx 0 \qquad (c.1i)
\end{align*}
$$

$$
\begin{align*}
&\Delta V_n^2 = V_n'^2 - V_n^2 \\
&\le \Delta V_{n-1}^2 \le \dots \le \Delta V_o^2 \approx 0 \qquad (c.1ii)
\end{align*}
$$

If we assume that $V_k' = V_k$, $V_n' = V_n$ and also that the change in power leaving the loop, such as $P_{io}$, $Q_{io}$ shown in the figure, are negligible, then the power flow in the loop can be updated by using the backward update starting from the nodes $k$ and $n$ of the loop. Since the voltage and power at these points are known, the corresponding quantities can be calculated at the points, $k-1, n-1$, by using the backward equations. Repeating this process up to node 0, the common node, we get the updated values

$$
\begin{align*}
&\hat{P}_i', \hat{Q}_i', \hat{V}_i', \quad i \in L \cup R \qquad (c.2)
\end{align*}
$$

Scheme 2: The approximations for the new power flows obtained by scheme 1 use the exact branch equations except the voltages the the terminal nodes ($V_k$ instead of $V'_k$, $V_n$ instead of $V'_n$). However, the error in voltages, $\Delta V_k^2$, $\Delta V_n^2$, being the biggest as indicated by Eq.(c.1), is carried back to the other nodes by backward voltage update of Eq.(2.iii). Therefore, this is not good. A better approach will be dropping the voltage update and instead using the original voltages; thus only the power updates (Eq.(2.i) and Eq.(2.ii)) are carried out.

Scheme 3: Since the accuracy of the backward update depends critically on the voltage estimate at the loop terminal nodes $n$ and $k$, it is desirable to check on the value of voltage difference, $\Delta V_k$, $\Delta V_n$ and correct the approximation, if necessary, to improve the estimation.

To estimate $\Delta V_k$, $\Delta V_n$, we will use the following property. Consider the radial network of Fig.3 again and let us calculate the change in total voltage drop across the network, $V_{o-n}^2 = V_o^2 - V_o^2$ as a result of a power change at the end of the network, $\Delta P_n$, $\Delta Q_n > 0$, by using simplified Dist-Flow equations in two different ways. Fist, as it is done in the Appendix B, by assuming that $V_o = V_o$ and by using the simplified forward voltage equation of Eq. (6.iii). Then the voltage drop can be calculated as $(\Delta V_{o-n}^2 - V = -\Delta V_o^2$. Second, by assuming $V_o' = V_o$ and by using the simplified backward equations $V_{o-1}^2 = V_o^2 = 2\tau_o P_i' + x_o Q_i$, and calculating the corresponding voltage change as $(\Delta V_{o-n}^2)^b = \Delta V_o^2$. It can be shown that these two estimates are equal to each other, i.e.

$$
\begin{align*}
(\Delta V_{o-n}^2)^f &= (\Delta V_{o-n}^2)^b 
\end{align*}\qquad (c.3)
$$


The results indicate that a good estimate of voltage change at the terminal nodes $n$ and $k$ can be obtained by carrying out the voltage update separately from the power update, while performing the backward update and comparing the voltage difference at node 0 (difference between $V_0$ and the updated $V_0$). If the difference is too large (larger than a predefined value, $\varepsilon^{\max}$), one may go through a forward update to reduce the error (this time starting from the common node $o$ and using $V_o, \hat{P}'_{ak}, \hat{P}'_{on}$ as initial, given values and applying the forward update).

We use scheme 3 as the second method of updating the power flows around the loop of a branch exchange.

Mesut E. Baran received his B.S. and M.S. form Middle East Technical University, Turkey. He is currently a Ph.D. student at the University of California, Berkeley. His research interests include distribution and power systems, optimization, system theory, and control theory.

Felix F. Wu received his B.S. from National Taiwan University, M.S. from the University of Pittsburgh, and Ph.D. from the University of California, Berkeley. He is a Professor of Electrical Engineering and Computer Sciences at the University of California, Berkeley.

---
[TOC]