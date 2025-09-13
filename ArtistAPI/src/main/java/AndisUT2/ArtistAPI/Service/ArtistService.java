package AndisUT2.ArtistAPI.Service;

import AndisUT2.ArtistAPI.Model.Artist;
import AndisUT2.ArtistAPI.Repository.ArtistRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ArtistService {

    private final ArtistRepository artistRepository;

    public ArtistService(ArtistRepository artistRepository) { this.artistRepository = artistRepository; }

    public Artist getArtistByName(String name){
        return artistRepository.getArtistByName(name);
    }

    public List<Artist> getAllArtists(){
        return artistRepository.getAllArtists();
    }

    public Artist getArtistById(int id){
        return artistRepository.getArtistById(id);
    }

    public List<Artist> getAllArtistsByGenre(String genre){
        return artistRepository.getArtistsByGenre(genre);
    }

    public Artist saveArtist(String name){
        Artist artist = new Artist(name);
        return artistRepository.saveArtist(artist);

    }

    public Artist saveArtistWGenre(String name, String genre){
        Artist artist = new Artist(name, genre);
        return artistRepository.saveArtist(artist);

    }
}
