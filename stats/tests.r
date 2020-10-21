library(MASS)

setwd("~/Documents/Repositories/islander-data/stats")

#test_data <- read.csv("collated.csv")
#View(test_data)

cancer_data <- matrix(c(0, 624, 18, 572, 31, 536, 24, 399), ncol = 4)
colnames(cancer_data) <- c("Non-Smoker", "Light Smoker", "Moderate Smoker", "Heavy Smoker")
rownames(cancer_data) <- c("Cancer", "No Cancer")
cancer_data <- as.table(cancer_data)
print(cancer_data)

colours.names = c("orange", "pink")
names = c("Non-Smoker", "Light Smoker", "Moderate Smoker", "Heavy Smoker")

png(filename="bars.png", width=700, height=700)
barplot(cancer_data, beside=T, axis.lty="solid", ylim=c(0, 700), names=names, col=colours, xlab="Level of smoking", ylab="Frequency", main="Frequency of cancer-having and\n non-cancer-having persons for given\n treatments of smoking")
legend("topright", rownames(cancer_data), cex=0.8, fill=colours, title="Cancer")
dev.off()

print(chisq.test(cancer_data))