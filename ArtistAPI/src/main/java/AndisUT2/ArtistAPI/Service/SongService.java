package AndisUT2.ArtistAPI.Service;

import AndisUT2.ArtistAPI.Model.Song;
import AndisUT2.ArtistAPI.Repository.SongRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SongService {


    private SongRepository songRepository;

    public SongService(SongRepository songRepository) {
        this.songRepository = songRepository;
    }

    public Song getSongById(int id) {
        return songRepository.getSongByID(id);
    }

    public Song getSongByName(String name) {
        return songRepository.getSongByName(name);
    }

    public List<Song> getAllSongs() {
        return songRepository.getAllSongs();
    }

    public List<Song> getSongsByArtistId(int artistId) {
        return songRepository.getSongsByArtistID(artistId);
    }

    public List<Song> getSongsByAlbumId(int albumId) {
        return songRepository.getSongsByAlbumID(albumId);
    }
}
