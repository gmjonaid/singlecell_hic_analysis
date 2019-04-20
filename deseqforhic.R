library(DESeq2)
countdata <- read.table("gm12878_name.txt", header=F, row.names=1)
colnames(countdata) <- c("gm12878_01", "gm12878_03","gm12878_04",
                         "gm12878_05","gm12878_06","gm12878_07","gm12878_09","gm12878_10",
                         "gm12878_11","gm12878_12", "gm12878_13", "gm12878_14","gm12878_15",
                         "gm12878_16","gm12878_17")

countdata <- as.matrix(countdata)
condition <- factor(c(rep("exp", 8), rep("ctl", 7)))
coldata <- data.frame(row.names=colnames(countdata), condition)
dds <- DESeqDataSetFromMatrix(countData=countdata, colData=coldata, design=~condition)

dds <- DESeq(dds)
plotDispEsts(dds, main="Dispersion plot")
res <- results(dds)
table(res$padj<0.05)
res <- res[order(res$padj), ]
resdata <- merge(as.data.frame(res), as.data.frame(counts(dds, normalized=TRUE)), by="row.names", sort=FALSE)
names(resdata)[1] <- "Gene"
write.csv(resdata, file="diffexpr-results.csv")

