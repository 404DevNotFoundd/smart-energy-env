# Smart Energy Distribution Environment ⚡

## Description
This project simulates a real-world smart grid where an AI agent distributes electricity across multiple regions to optimize efficiency and minimize energy imbalance.

## Motivation
Modern cities face energy demand fluctuations leading to power inefficiencies. This environment helps train AI agents to solve dynamic energy allocation problems.

## Observation Space
- Region demands (list)
- Available power
- Time step

## Action Space
- Allocation of power to each region

## Reward Function
- Score between 0.0 – 1.0
- Based on how well allocation matches demand
- Penalizes overload and inefficiency

## Tasks
- Easy: 2 regions
- Medium: 3 regions
- Hard: 5 regions

## Setup
```bash
docker build -t energy-env .
docker run energy-env