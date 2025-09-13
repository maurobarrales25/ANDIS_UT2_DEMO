package AndisUT2.ArtistAPI.Service;

import AndisUT2.ArtistAPI.Model.Album;
import AndisUT2.ArtistAPI.Model.Artist;
import AndisUT2.ArtistAPI.Repository.AlbumRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AlbumService {

    private final AlbumRepository albumRepository;

    private final ArtistService artistService;

    public AlbumService(AlbumRepository albumRepository, ArtistService artistService) {
        this.albumRepository = albumRepository;
        this.artistService = artistService;
    }

    public Album getAlbumByName(String name){
        return albumRepository.getAlbumByName(name);
    }

    public Album getAlbumById(int id){
        return albumRepository.getAlbumById(id);
    }

    public List<Album> getAllAlbums(){
        return albumRepository.getAllAlbums();
    }

    public List<Album> getAlbumsByArtistId(int artistId){
        return albumRepository.getAlbumsByArtistId(artistId);
    }

    public Album saveAlbum(String name, String artistName){
       Artist artist = artistService.getArtistByName(artistName);
       if(artist == null){
           Artist newArtist = artistService.saveArtist(artistName);
           Album album = new Album();
           album.setAlbumName(name);
           album.setArtistId(newArtist.getArtistID());
       }

       Album album = new Album(name, artist.getArtistID());
       return albumRepository.saveAlbum(album);
    }

}
