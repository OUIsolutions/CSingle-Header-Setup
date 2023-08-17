

void *write_file(const char *path, const char *content){

        FILE *file = fopen(path, "w");
        if(!file){
            return;
        }
        fprintf(file,"%s",content);
        fclose(file);
}