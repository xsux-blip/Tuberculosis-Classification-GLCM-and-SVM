library(dplyr)
library(ggplot2)
library(treemap)
library(readr)
library(tibble)

# Mengubah rownames menjadi kolom, kemudian menghapus rownames
dataset <- dataset %>% rownames_to_column(var = "rowname")


dataset <- read.csv("J:/proyek/USRegionalMortality.csv")
dataset

glimpse(dataset)
summary(dataset)

dataset <- dataset %>% remove_rownames()


# 4. Plotting Treemap dari Rata-rata Tingkat Kematian Berdasarkan Wilayah


region_avg <- dataset %>%
  group_by(Region) %>%
  summarize(avg_rate = mean(Rate, na.rm = TRUE))

treemap(region_avg, 
        index = "Region", 
        vSize = "avg_rate", 
        vColor = "avg_rate", 
        type = "value", 
        title = "Treemap of Average Mortality Rate by Region")


# 6. Plotting Treemap dari Rata-rata Tingkat Kematian Berdasarkan Jenis Kelamin
sex_avg <- dataset %>%
  group_by(Sex) %>%
  summarize(avg_rate = mean(Rate, na.rm = TRUE))

treemap(sex_avg, 
        index = "Sex", 
        vSize = "avg_rate", 
        vColor = "avg_rate", 
        type = "value", 
        title = "Treemap of Average Mortality Rate by Sex")

# 7. Plotting Treemap dari Rata-rata Tingkat Kematian Berdasarkan Penyebab Kematian
cause_avg <- dataset %>%
  group_by(Cause) %>%
  summarize(avg_rate = mean(Rate, na.rm = TRUE))

treemap(cause_avg, 
        index = "Cause", 
        vSize = "avg_rate", 
        vColor = "avg_rate", 
        type = "value", 
        title = "Treemap of Average Mortality Rate by Cause of Death")

# 8. Bar Plot dari Wilayah, Status, Jenis Kelamin, dan Penyebab vs Tingkat Kematian

ggplot(dataset, aes(x = Region, y = Rate, fill = Status)) +
  geom_bar(stat = "identity", position = "dodge") +
  facet_wrap(~ Sex + Cause) +
  labs(title = "Bar Plot of Mortality Rate by Region, Status, Sex, and Cause of Death",
       x = "Region", y = "Mortality Rate") +
  theme_minimal()
# 9. Bar Plots dari Status, Jenis Kelamin, dan Penyebab vs Tingkat Kematian untuk Semua Wilayah

ggplot(dataset, aes(x = Status, y = Rate, fill = Cause)) +
  geom_bar(stat = "identity", position = "dodge") +
  facet_wrap(~ Region + Sex) +
  labs(title = "Bar Plot of Mortality Rate by Status, Sex, Cause of Death for All Regions",
       x = "Status", y = "Mortality Rate") +
  theme_minimal()

