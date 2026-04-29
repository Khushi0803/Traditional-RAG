from rag_pipeline import (
    process_all_pdfs,
    split_documents,
    EmeddingManager,
    VectorStore,
    RAGRetriever,
    rag_simple,
    llm
)


def main():
    print("Hello from rag-new!")

 # Process all PDFs in the data directory
    all_pdf_documents = process_all_pdfs("data")

    all_pdf_documents


    chunks=split_documents(all_pdf_documents)
    chunks

    ## initialize the emedding manager":

    emedding_manager=EmeddingManager()
    emedding_manager

    vectorstore=VectorStore()
    vectorstore

    chunks

    #convert the text into emeddings
    texts = [doc.page_content for doc in chunks]

    #convert emeddings
    emeddings = emedding_manager.generate_emeddings(texts)

    vectorstore.add_documents(chunks,emeddings)

    rag_retriever = RAGRetriever(vectorstore ,emedding_manager)

                
    rag_retriever.retrieve("If the company sponsors an employee’s certification, what service commitment may be required?")
    answer=rag_simple("Why is onboarding training mandatory for new employees and how does it affect probation confirmation?",rag_retriever,llm)
    print(answer)




if __name__ == "__main__":
    main()
