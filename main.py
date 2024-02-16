import param
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
generation = 1
population = []
found = False
plot_fitness = []
plot_gen = []

for x in range(param.num_pop):  # initialize first population
    empty_chromosome = param.create_crom()
    population.append(empty_chromosome)
population = param.sort_strings_by_fitness(population)

while not found:

    population = param.sort_strings_by_fitness(population)  # sort list with lowest finest first

    if (param.cal_fitness(list(population[0])) <= 0) or generation == param.num_genes:  # break the while if the solution is found or the maximum generation is reached
        found = True
        break

    new_generation = param.create_offspring(population, population) # make the new population

    population = new_generation # Save the new polulation for the next loop


    plot_fitness.append(param.cal_fitness(population[0])) # save the data for the plot
    plot_gen.append(generation)# save the data for the plot
    print("Generations: ", generation,"Result: ", "".join(list(population[0])))

    generation = generation + 1

fig, ax = plt.subplots()
ax.plot(plot_gen, plot_fitness)
# Change x-axis and y-axis tick spacing
ax.xaxis.set_major_locator(ticker.MultipleLocator(base=2))  # x-axis ticks at multiples of 2
ax.yaxis.set_major_locator(ticker.MultipleLocator(base=1))  # y-axis ticks at multiples of 0.5
plt.xlabel("Generations")
plt.ylabel("Fitness")

plt.grid()
plt.show()

print("Result: ", "".join(list(population[0])), "Gen: ", generation, "fitness: ",
      param.cal_fitness(list(population[0])))
