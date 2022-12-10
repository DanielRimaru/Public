files <- c("brands.csv", "distribution.csv", "traits.csv", "traits_small.csv")
#saving the file names
folderPath <- "C:/Users/Dani-PC/Desktop/Covatic-Data"
#saving the path to the Covatic-Data folder

filePaths <- paste(folderPath,files ,sep = "/")
#saving the filepaths

brandsDf <- read.csv(filePaths[1])
distributionDf <- read.csv(filePaths[2],skip  =0, header = FALSE, col.names = c("Type", "Percentage"))
traitsDf <- read.csv(filePaths[3])
traitsTestingDf <- read.csv(filePaths[4])


library(e1071) 
library("explore")
library("ggplot2")
#explore(traitsTestingDf)
#explore(brandsDf)


basicStats <- function(coll){
  return (cat(paste("Dani's report on the given column: ",
                "\n Mean value:         ", mean(coll), 
                "\n Standard Deviation: ", sd(coll), 
                "\n Range:              ", min(coll), "   -  ", max(coll), 
                "\n Skewness:           ", skewness(coll))))
}



multiply <- function(string, times){
  ret <- c()
  for(i in 1:times){
    ret <- c(ret, string)
  }
  return (ret)
}




categories <-c("1. Affluent	Achievers", "2. Rising Prosperity", "3. Comfortable	Communities", "4. Financially	Stretched", "5. Urban	Adversity")
catpercentages <- c(sum(distributionDf[1:13,2]),sum(distributionDf[14:20,2]),sum(distributionDf[21:33,2]),sum(distributionDf[34:48,2]),sum(distributionDf[49:59,2]))
distCatDf <- data.frame(Category = categories ,
                        Percentage = catpercentages)





brandsDfTransposed <- as.data.frame(t(brandsDf))
#working with the transposed version because it's easier uwu :3

brandsDfTransposed[is.na(brandsDfTransposed)] <- 0
#there are some missing values for some brands
#explore(brandsDfTransposed)





brandsCatDf <- data.frame("1.Affluent Achievers" = colMeans(brandsDfTransposed[1:13,]),
                          "2.Rising Prosperity" = colMeans(brandsDfTransposed[14:20,]),
                          "3.Comfortable	Communities" = colMeans(brandsDfTransposed[21:33,]),
                          "4.Financially	Stretched" = colMeans(brandsDfTransposed[34:48,]),
                          "5.Urban	Adversity" = colMeans(brandsDfTransposed[49:59,])
                          )



brandsCatDfTransposed <- as.data.frame(t(brandsCatDf))

p <- ggplot(data=distributionDf, aes(x=factor(Type), y=Percentage, fill=factor(Type)))+
  geom_bar(stat= "identity", width = 0.5)+
  scale_fill_manual(values = c(multiply("#304B9E",13),multiply("#684FA1",7),
                                multiply("#376E36",13),multiply("#C1C632",15),
                                multiply("#1C687B",11)))+
  theme(legend.position="none",
        plot.title=element_text(hjust = 0.5))+
  labs(x="Type",
       title= "Population types frequency in terms of the percentage they represent")

  
p

pcat<- ggplot(data=distCatDf, aes(x=Category, y=Percentage, fill=Category))+
  geom_bar(stat= "identity", width = 0.5)+
  scale_fill_manual(values = c("#304B9E","#684FA1",
                               "#376E36","#C1C632",
                               "#1C687B"))+
  theme(legend.position="none",
        plot.title=element_text(hjust = 0.5))+
  labs(x="Category",
       title= "Population category frequency in terms of the percentage they represent")

pcat
q <- ggplot(data=brandsDfTransposed, aes(x=factor(as.numeric(sub('.','',rownames(brandsDfTransposed)))), y=rowSums(brandsDfTransposed), fill=factor(as.numeric(sub('.','',rownames(brandsDfTransposed))))  ))+
  geom_bar(stat= "identity", width = 0.5)+
  scale_fill_manual(values = c(multiply("#304B9E",13),multiply("#684FA1",7),
                               multiply("#376E36",13),multiply("#C1C632",15),
                               multiply("#1C687B",11)))+
  theme(legend.position="none",
        plot.title=element_text(hjust = 0.5))+
  labs(x="Type",
       y="",
       title= "Population types frequency as they show up in the brands users.")

q


hist(cacidist, xlab= "UK population percentage", ylab="Number of types", main="CACI Percentage frequency Distribution", col= "green")

#mean(distributionDf$Percentage)

#22 & 26 > 3%
#1, 30, 34 < 0.5%



hist(brandsDfTransposed$V1, breaks= 3, xlab= "User amount", ylab="Number of acorns", main=paste("Acorn Distribution based on the amount of users for brand 1"))
max(brandsDfTransposed$V1)
which.max(brandsDfTransposed$V1)


boxplot(brandsDfTransposed, xlab = "Brands ", ylab= "Number of users", main="User distribution for each brand", col="red")
#V6 and V7 are very niche!

max(brandsDfTransposed$V6)
which.max(brandsDfTransposed$V6)
max(brandsDfTransposed$V7)
which.max(brandsDfTransposed$V7)


boxplot(brandsDfTransposed$V7, xlab = "Brands ", ylab= "Number of users", main="User distribution for each brand")
#inspecting Brand 7 in particular, X18, X19, X34, X39 are the target audience 





traitsTestingDfTransposed <- as.data.frame(t(traitsTestingDf))
#explore(traitsTestingDfTransposed)


boxplot(traitsTestingDfTransposed, xlab = "Acorns ", ylab= "Trait relevance", main="Trait relevance for each acorn")
max(traitsTestingDfTransposed$V1)
which.max(traitsTestingDfTransposed$V1)


traitsDfTransposed <- as.data.frame(t(traitsDf))
boxplot(traitsDfTransposed, xlab = "Acorns ", ylab= "Trait relevance", main="Trait relevance for each acorn")

#1. Is there any advantage in picking a certain type as the target audience?
#
#1. Do users from similar financial backgrounds (categories) buy the same product?
#2. Does type percentage have any impact on the amount of users for the brands from each type?
#3. Are very polarizing brands(brands with high variance) targeted at affluent customers?
#4. Are products aimed at rich people also bought by the less affluent ones?
#5. Are targeted products more popular than general use products? (two sample t-test)




#create df
#find unique values

#frequency in x in terms of y ()

#counting user quantity(%) in terms of income bracket   


t.test(brandsDfTransposed$V4, brandsCatDfTransposed$V4, alternative = "greater", var.equal =TRUE)


e<- as.data.frame(rowSums(brandsDfTransposed)/sum(brandsDfTransposed) * 100)

covaticdist <- round(e$`rowSums(brandsDfTransposed)/sum(brandsDfTransposed) * 100`,4)
cacidist <- distributionDf$Percentage

data <- data.frame("Type" = 1:59,
                   "COVATIC PERCENTAGES" = covaticdist,
                   "CACI Percentages" = cacidist)


diff <- data$COVATIC.PERCENTAGES - data$CACI.Percentages
skewness(diff)



shapiro.test(data$COVATIC.PERCENTAGES)
shapiro.test(data$CACI.Percentages)
t.test(covaticdist,cacidist, paired= TRUE ,alternative = "two.sided") #but the covatic % are not normally distributed so we will be using wilcoxon instead
wilcox.test(data$COVATIC.PERCENTAGES, data$CACI.Percentages, paired = TRUE, alternative = "two.sided")


lmrich <- lm(X1.Affluent.Achievers~X5.Urban.Adversity, brandsCatDf)
summary(lmrich)

