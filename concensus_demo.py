import random

miners = {
    "MinerAlpha": random.randint(10, 100),
    "MinerBeta": random.randint(10, 100),
    "MinerGamma": random.randint(10, 100)
}

pow_winner = max(miners, key=miners.get)
print("\n--- Proof of Work (PoW) ---")
print("Mining Powers:", miners)
print(f"Selected Validator: {pow_winner} (Power: {miners[pow_winner]})")
print("Reason: Highest computational power wins the block reward.\n")


stakers = {
    "StakerAlice": random.randint(100, 1000),
    "StakerBob": random.randint(100, 1000),
    "StakerCarol": random.randint(100, 1000)
}

pos_winner = max(stakers, key=stakers.get)
print("--- Proof of Stake (PoS) ---")
print("Stakes:", stakers)
print(f"Selected Validator: {pos_winner} (Stake: {stakers[pos_winner]})")
print("Reason: Highest stake has the most economic interest and is selected.\n")


delegates = ["DelegateX", "DelegateY", "DelegateZ"]
voters = ["Voter1", "Voter2", "Voter3"]
votes = random.choices(delegates, k=len(voters))

vote_count = {delegate: votes.count(delegate) for delegate in delegates}
dpos_winner = max(vote_count, key=vote_count.get)

print("--- Delegated Proof of Stake (DPoS) ---")
print("Votes:", votes)
print("Vote Count:", vote_count)
print(f"Selected Delegate: {dpos_winner}")
print("Reason: Delegate with the most votes from stakeholders is chosen.\n")
