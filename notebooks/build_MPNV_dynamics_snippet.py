# Code snippet for build_MPNV_dynamics() -- the part where we build the dynamics object

    # Build the `dynamics` dict:
    # 	for each s in the state space:
    #   	for each a in the action space such that s + a is in the state space: 
    #       	for each demand d such that s + a - d is in the state space:
    #           	set dynamics[s, a][s_prime, r] = P(D = d) for the appropriate
    #           	values of s_prime and r (where P(D = d) is the probability that
    #           	the demand equals d)
    dynamics = {}
    for s in state_space:
        for a in action_space:
            # Make sure OUL is within state space truncation.
            if s + a in state_space:
                dynamics[s, a] = {}
                # Only consider demands that would not take us past the minimum state.
                for d in range(s + a - min_state + 1):
                    oul = s + a
                    s_prime = oul - d
                    r = -(h * max(0, oul - d) + p * max(0, d - oul))
                    dynamics[s, a][s_prime, r] = poisson.pmf(d, mu)
