package AndisUT2.ArtistAPI.Controller;

import AndisUT2.ArtistAPI.Model.Album;
import AndisUT2.ArtistAPI.Service.AlbumService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/album")
public class AlbumController {

    @Autowired
    private AlbumService albumService;

    @GetMapping("/all")
    public ResponseEntity<List<Album>> getAllAlbums(){
        List<Album> albums = albumService.getAllAlbums();
        return albums.isEmpty()
                ? ResponseEntity.noContent().build()
                : ResponseEntity.ok(albums);
    }

    @GetMapping("/by-name")
    public ResponseEntity<Album> getAlbumByName(@RequestParam String name){
        Album album = albumService.getAlbumByName(name);
        return ResponseEntity.ok(album);
    }

    @GetMapping("by-id")
    public ResponseEntity<Album> getAlbumById(@RequestParam int id){
        Album album = albumService.getAlbumById(id);
        return ResponseEntity.ok(album);
    }

    @GetMapping("/by-artist-id")
    public ResponseEntity<List<Album>> getAlbumByArtistId(@RequestParam int id){
        List<Album> albums = albumService.getAlbumsByArtistId(id);
        return albums.isEmpty()
                ? ResponseEntity.noContent().build()
                : ResponseEntity.ok(albums);
    }

    @PostMapping("/save")
    public ResponseEntity<Album> saveAlbum(@RequestParam String albumName, String artistName){
        Album album = albumService.saveAlbum(albumName, artistName);
        return ResponseEntity.ok(album);
    }

}
