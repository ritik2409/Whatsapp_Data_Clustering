# README #

├──server 

           ├──__init__.py                  
           ├── app.py                    			# Main File to run flask API and call different scripts
           ├── cleaning.py                     	    # Cleaning of the text file
           ├── config.py                    		# Storing system and upload folder path
           ├── whatsapp_clusters.py 				#Clustering of text file
	       ├── templates
		   ├── template.html				        # Flask API template
	       ├──	Upload_folder					    # Folder is used to upload text and write final clustered text files
           ├── GoogleNews-vectors-negative300.bin   #Google Pretrained Word2Vec Model
├── Dockerfile 

└─ README.md

                     =============================================================================
### From where to download google pretrained model?
 * [Google Word2Vec Model](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit)
 * Store it in the server folder
