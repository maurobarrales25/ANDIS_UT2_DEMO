package AndisUT2.ArtistAPI.Config;

import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.info.Info;
import org.springframework.context.annotation.Configuration;

@Configuration
@OpenAPIDefinition(info = @Info(
        title = "Artist API",
        version = "1.0",
        description = "UT2 - DEMO"
))


public class OpenAPIConfig {
}
